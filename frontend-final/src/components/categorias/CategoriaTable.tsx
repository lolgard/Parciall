import type { Categoria } from "../../types/categoria"

interface Props {
  categorias: Categoria[]
  onEditar: (cat: Categoria) => void
  onEliminar: (id: number) => void
}

function CategoriaTable({ categorias, onEditar, onEliminar }: Props) {
  return (
    <table className="w-full border-collapse bg-white rounded-xl shadow overflow-hidden">
      <thead className="bg-gray-100">
        <tr>
          <th className="text-left px-4 py-3 text-gray-600">ID</th>
          <th className="text-left px-4 py-3 text-gray-600">Nombre</th>
          <th className="text-left px-4 py-3 text-gray-600">Descripción</th>
          <th className="text-left px-4 py-3 text-gray-600">Imagen</th>
          <th className="text-left px-4 py-3 text-gray-600">Acciones</th>
        </tr>
      </thead>
      <tbody>
        {categorias.length === 0 ? (
          <tr>
            <td colSpan={5} className="px-4 py-6 text-center text-gray-400">
              No hay categorías cargadas
            </td>
          </tr>
        ) : (
          categorias.map((cat) => (
            <tr key={cat.id} className="border-t hover:bg-gray-50">
              <td className="px-4 py-3 text-gray-800">{cat.id}</td>
              <td className="px-4 py-3 font-medium text-gray-800">{cat.nombre}</td>
              <td className="px-4 py-3 text-gray-500">{cat.descripcion}</td>
              <td className="px-4 py-3 text-gray-500">{cat.imagen_url}</td>
              <td className="px-4 py-3 flex gap-2">
                <button
                  onClick={() => onEditar(cat)}
                  className="bg-yellow-400 text-white px-3 py-1 rounded hover:bg-yellow-500 text-sm"
                >
                  Editar
                </button>
                <button
                  onClick={() => onEliminar(cat.id)}
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

export default CategoriaTable
