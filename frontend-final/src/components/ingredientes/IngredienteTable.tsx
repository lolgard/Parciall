import type { Ingrediente } from "../../types/ingredientes"

interface Props {
  ingredientes: Ingrediente[]
  onEditar: (ing: Ingrediente) => void
  onEliminar: (id: number) => void
}

function IngredienteTable({ ingredientes, onEditar, onEliminar }: Props) {
  return (
    <table className="w-full border-collapse bg-white rounded-xl shadow overflow-hidden">
      <thead className="bg-gray-100">
        <tr>
          <th className="text-left px-4 py-3 text-gray-600">ID</th>
          <th className="text-left px-4 py-3 text-gray-600">Nombre</th>
          <th className="text-left px-4 py-3 text-gray-600">Descripción</th>
          <th className="text-left px-4 py-3 text-gray-600">Alérgeno</th>
          <th className="text-left px-4 py-3 text-gray-600">Acciones</th>
        </tr>
      </thead>
      <tbody>
        {ingredientes.length === 0 ? (
          <tr>
            <td colSpan={5} className="px-4 py-6 text-center text-gray-400">
              No hay ingredientes cargados
            </td>
          </tr>
        ) : (
          ingredientes.map((ing) => (
            <tr key={ing.id} className="border-t hover:bg-gray-50">
              <td className="px-4 py-3">{ing.id}</td>
              <td className="px-4 py-3 font-medium">{ing.name}</td>
              <td className="px-4 py-3 text-gray-500">{ing.description}</td>
              <td className="px-4 py-3">
                <span className={`px-2 py-1 rounded-full text-xs font-semibold ${ing.esAlergeno ? "bg-red-100 text-red-700" : "bg-green-100 text-green-700"}`}>
                  {ing.esAlergeno ? "Sí" : "No"}
                </span>
              </td>
              <td className="px-4 py-3 flex gap-2">
                <button
                  onClick={() => onEditar(ing)}
                  className="bg-yellow-400 text-white px-3 py-1 rounded hover:bg-yellow-500 text-sm"
                >
                  Editar
                </button>
                <button
                  onClick={() => onEliminar(ing.id)}
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

export default IngredienteTable
