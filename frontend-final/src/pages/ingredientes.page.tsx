import { useState } from "react"
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query"
import { getIngredientes, createIngrediente, updateIngrediente, deleteIngrediente } from "../services/ingrediente.service"
import type{ Ingrediente, IngredienteCreate } from "../types/ingredientes"

interface ModalProps {
  inicial: IngredienteCreate
  onGuardar: (data: IngredienteCreate) => void
  onCerrar: () => void
  titulo: string
}

function Modal({ inicial, onGuardar, onCerrar, titulo }: ModalProps) {
  const [form, setForm] = useState<IngredienteCreate>(inicial)

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="bg-white rounded-xl p-6 w-full max-w-md shadow-xl">
        <h2 className="text-xl font-bold mb-4">{titulo}</h2>
        <div className="flex flex-col gap-3">
          <input
            className="border rounded-lg px-3 py-2"
            placeholder="Nombre"
            value={form.name}
            onChange={(e) => setForm({ ...form, name: e.target.value })}
          />
          <input
            className="border rounded-lg px-3 py-2"
            placeholder="Descripción"
            value={form.description}
            onChange={(e) => setForm({ ...form, description: e.target.value })}
          />
          <label className="flex items-center gap-2 cursor-pointer">
            <input
              type="checkbox"
              checked={form.esAlergeno}
              onChange={(e) => setForm({ ...form, esAlergeno: e.target.checked })}
            />
            <span>Es alérgeno</span>
          </label>
        </div>
        <div className="flex gap-2 mt-5 justify-end">
          <button onClick={onCerrar} className="px-4 py-2 rounded-lg border hover:bg-gray-100">Cancelar</button>
          <button onClick={() => onGuardar(form)} className="px-4 py-2 rounded-lg bg-blue-600 text-white hover:bg-blue-700">Guardar</button>
        </div>
      </div>
    </div>
  )
}

function IngredientesPage() {
  const queryClient = useQueryClient()
  const [modalAbierto, setModalAbierto] = useState(false)
  const [editando, setEditando] = useState<Ingrediente | null>(null)

  const { data: ingredientes = [], isLoading } = useQuery({
    queryKey: ["ingredientes"],
    queryFn: getIngredientes,
  })

  const crearMutation = useMutation({
    mutationFn: createIngrediente,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["ingredientes"] })
      setModalAbierto(false)
    },
  })

  const editarMutation = useMutation({
    mutationFn: ({ id, data }: { id: number; data: IngredienteCreate }) => updateIngrediente(id, data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["ingredientes"] })
      setEditando(null)
    },
  })

  const eliminarMutation = useMutation({
    mutationFn: deleteIngrediente,
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ["ingredientes"] }),
  })

  const handleGuardar = (data: IngredienteCreate) => {
    if (editando) {
      editarMutation.mutate({ id: editando.id, data })
    } else {
      crearMutation.mutate(data)
    }
  }

  if (isLoading) return <p className="p-8 text-gray-500">Cargando ingredientes...</p>

  return (
    <div className="p-8">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-gray-800">Ingredientes</h1>
        <button
          onClick={() => setModalAbierto(true)}
          className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
        >
          + Nuevo Ingrediente
        </button>
      </div>

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
            ingredientes.map((ing: Ingrediente) => (
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
                    onClick={() => setEditando(ing)}
                    className="bg-yellow-400 text-white px-3 py-1 rounded hover:bg-yellow-500 text-sm"
                  >
                    Editar
                  </button>
                  <button
                    onClick={() => eliminarMutation.mutate(ing.id)}
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

      {modalAbierto && (
        <Modal
          titulo="Nuevo Ingrediente"
          inicial={{ name: "", description: "", esAlergeno: false }}
          onGuardar={handleGuardar}
          onCerrar={() => setModalAbierto(false)}
        />
      )}
      {editando && (
        <Modal
          titulo="Editar Ingrediente"
          inicial={{ name: editando.name, description: editando.description, esAlergeno: editando.esAlergeno }}
          onGuardar={handleGuardar}
          onCerrar={() => setEditando(null)}
        />
      )}
    </div>
  )
}

export default IngredientesPage