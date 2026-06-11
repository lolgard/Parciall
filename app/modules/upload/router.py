from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, status
from app.core.deps import require_role
from app.core.cloudinary import upload_image_to_cloudinary

router = APIRouter(prefix="/uploads", tags=["uploads"])

@router.post("/image", dependencies=[Depends(require_role(["ADMIN", "STOCK"]))])
async def upload_image(file: UploadFile = File(...)):
    """
    Sube una imagen al backend, la comprime usando Pillow y la envía a Cloudinary.
    Retorna la URL segura de la imagen.
    """
    # Validar formato del archivo
    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El archivo proporcionado no es una imagen válida."
        )
        
    try:
        # Leer los bytes de la imagen
        file_bytes = await file.read()
        
        # Subir a Cloudinary con compresión local previa
        image_url = upload_image_to_cloudinary(file_bytes, folder="foodstore_products")
        
        return {"image_url": image_url}
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al procesar o subir la imagen: {str(e)}"
        )
