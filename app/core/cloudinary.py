import os
import io
import cloudinary
import cloudinary.uploader
from PIL import Image

# Configurar Cloudinary usando variables de entorno
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)

def compress_image(file_bytes: bytes, max_size: int = 1000, quality: int = 80) -> bytes:
    """
    Lee los bytes de una imagen, la redimensiona si excede el tamaño máximo
    manteniendo la relación de aspecto, y la comprime en formato JPEG.
    """
    try:
        # Abrir la imagen desde bytes
        img = Image.open(io.BytesIO(file_bytes))
        
        # Convertir a RGB si es necesario (ej: PNGs con transparencia a JPG)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
            
        # Obtener dimensiones originales
        width, height = img.size
        
        # Redimensionar si es más grande que max_size
        if width > max_size or height > max_size:
            if width > height:
                new_width = max_size
                new_height = int(height * (max_size / width))
            else:
                new_height = max_size
                new_width = int(width * (max_size / height))
                
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
        # Guardar en un buffer de bytes en formato JPEG
        output_buffer = io.BytesIO()
        img.save(output_buffer, format="JPEG", quality=quality, optimize=True)
        return output_buffer.getvalue()
    except Exception as e:
        # Si algo falla durante la compresión, devolvemos los bytes originales
        print(f"Error comprimiendo imagen: {e}")
        return file_bytes

def upload_image_to_cloudinary(file_bytes: bytes, folder: str = "foodstore") -> str:
    """
    Comprime la imagen localmente y la sube a Cloudinary.
    Retorna la URL segura (HTTPS) del archivo subido.
    """
    # 1. Comprimir la imagen
    compressed_bytes = compress_image(file_bytes)
    
    # 2. Subir a Cloudinary
    result = cloudinary.uploader.upload(
        io.BytesIO(compressed_bytes),
        folder=folder,
        resource_type="image"
    )
    
    # Retornar la URL segura
    return result.get("secure_url")
