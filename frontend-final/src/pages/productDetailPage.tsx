import { useParams, useNavigate } from "react-router-dom"
import { useQuery } from "@tanstack/react-query"
import { getProductoById } from "../services/producto.service"

function ProductDetailPage() {
  const { id } = useParams()
  const navigate = useNavigate()

  const { data: producto, isLoading, isError } = useQuery({
    queryKey: ["producto", id],
    queryFn: () => getProductoById(Number(id)),
  })

  if (isLoading) return <p className="p-8 text-gray-500">Cargando producto...</p>
  if (isError || !producto) return <p className="p-8 text-red-500">Producto no encontrado</p>

  return (
    <div className="p-8 max-w-xl mx-auto">
      <button onClick={() => navigate(-1)} className="mb-4 text-blue-600 hover:underline">
        ← Volver
      </button>
      <div className="bg-white rounded-xl shadow p-6">
        <h1 className="text-2xl font-bold mb-4">{producto.name}</h1>
        <p className="text-gray-600">Precio: <span className="font-semibold">${producto.price}</span></p>
        <p className="text-gray-600">Stock: <span className="font-semibold">{producto.stock_cantidad}</span></p>
        <p className="text-gray-600">
          Disponible:
          <span className={`ml-2 px-2 py-1 rounded-full text-xs font-semibold ${producto.disponible ? "bg-green-100 text-green-700" : "bg-red-100 text-red-700"}`}>
            {producto.disponible ? "Sí" : "No"}
          </span>
        </p>
      </div>
    </div>
  )
}

export default ProductDetailPage
