import { useNavigate } from "react-router-dom"
import type { Producto } from "../../types/producto"
import type { Categoria } from "../../types/categoria"
import type { Ingrediente } from "../../types/ingredientes"

interface Props {
  productos: Producto[]
  categorias: Categoria[]
  ingredientes: Ingrediente[]
  onEditar: (prod: Producto) => void
  onEliminar: (id: number) => void
}

function ProductoTable({ productos, categorias, ingredientes, onEditar, onEliminar }: Props) {
  const navigate = useNavigate()

  return (
    <table className="w-full border-collapse bg-white rounded-xl shadow overflow-hidden">
      <thead className="bg-gray-100">
        <tr>
          <th className="text-left px-4 py-3 text-gray-600">ID</th>
          <th className="text-left px-4 py-3 text-gray-600">Nombre</th>
          <th className="text-left px-4 py-3 text-gray-600">Precio</th>
          <th className="text-left px-4 py-3 text-gray-600">Stock</th>
          <th className="text-left px-4 py-3 text-gray-600">Disponible</th>
          <th className="text-left px-4 py-3 text-gray-600">Categorías</th>
          <th className="text-left px-4 py-3 text-gray-600">Ingredientes</th>
          <th className="text-left px-4 py-3 text-gray-600">Acciones</th>
        </tr>
      </thead>
      <tbody>
        {productos.length === 0 ? (
          <tr>
            <td colSpan={8} className="px-4 py-6 text-center text-gray-400">
              No hay productos cargados
            </td>
          </tr>
        ) : (
          productos.map((prod) => (
            <tr key={prod.id} className="border-t hover:bg-gray-50">
              <td className="px-4 py-3">{prod.id}</td>
              <td className="px-4 py-3 font-medium">{prod.name}</td>
              <td className="px-4 py-3">${prod.price}</td>
              <td className="px-4 py-3">{prod.stock_cantidad}</td>
              <td className="px-4 py-3">
                <span className={`px-2 py-1 rounded-full text-xs font-semibold ${prod.disponible ? "bg-green-100 text-green-700" : "bg-red-100 text-red-700"}`}>
                  {prod.disponible ? "Sí" : "No"}
                </span>
              </td>
              <td className="px-4 py-3">
                {prod.categorias?.map((c) => categorias.find((cat) => cat.id === c.categoria_id)?.nombre).join(", ")}
              </td>
              <td className="px-4 py-3">
                {prod.ingredientes?.map((i) => ingredientes.find((ing) => ing.id === i.ingrediente_id)?.name).join(", ")}
              </td>
              <td className="px-4 py-3 flex gap-2">
                <button
                  onClick={() => navigate(`/productos/${prod.id}`)}
                  className="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600 text-sm"
                >
                  Ver
                </button>
                <button
                  onClick={() => onEditar(prod)}
                  className="bg-yellow-400 text-white px-3 py-1 rounded hover:bg-yellow-500 text-sm"
                >
                  Editar
                </button>
                <button
                  onClick={() => onEliminar(prod.id)}
                  className="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600 text-sm"
                >
                  Eliminar
                </button>
              </td>
            </tr>
          ))
        )}
      </tbody>
    </table>
  )
}

export default ProductoTable
