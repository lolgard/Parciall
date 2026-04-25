import { useState } from "react"
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query"
import { getCategorias, createCategoria, updateCategoria, deleteCategoria } from "../services/categoria.service"
import type { Categoria, CategoriaCreate } from "../types/categoria"

interface ModalProps {
  inicial: CategoriaCreate
  onGuardar: (data: CategoriaCreate) => void
  onCerrar: () => void
  titulo: string
}

function Modal({ inicial, onGuardar, onCerrar, titulo }: ModalProps) {
  const [form, setForm] = useState<CategoriaCreate>(inicial)

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="bg-white rounded-xl p-6 w-full max-w-md shadow-xl">
        <h2 className="text-xl font-bold mb-4 text-gray-800">{titulo}</h2>
        <div className="flex flex-col gap-3">
          <input
            className="border rounded-lg px-3 py-2 text-gray-800"
            placeholder="Nombre"
            value={form.nombre}
            onChange={(e) => setForm({ ...form, nombre: e.target.value })}
          />
          <input
            className="border rounded-lg px-3 py-2 text-gray-800"
            placeholder="Descripción"
            value={form.descripcion}
            onChange={(e) => setForm({ ...form, descripcion: e.target.value })}
          />
          <input
            className="border rounded-lg px-3 py-2 text-gray-800"
            placeholder="URL de imagen"
            value={form.imagen_url}
            onChange={(e) => setForm({ ...form, imagen_url: e.target.value })}
          />
        </div>
        <div className="flex gap-2 mt-5 justify-end">
          <button onClick={onCerrar} className="px-4 py-2 rounded-lg border hover:bg-gray-100 text-gray-800">Cancelar</button>
          <button onClick={() => onGuardar(form)} className="px-4 py-2 rounded-lg bg-blue-600 text-white hover:bg-blue-700">Guardar</button>
        </div>
      </div>
    </div>
  )
}

function CategoriasPage() {
  const queryClient = useQueryClient()
  const [modalAbierto, setModalAbierto] = useState(false)
  const [editando, setEditando] = useState<Categoria | null>(null)

  const { data: categorias = [], isLoading, isError } = useQuery({
    queryKey: ["categorias"],
    queryFn: getCategorias,
  })

  const crearMutation = useMutation({
    mutationFn: createCategoria,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["categorias"] })
      setModalAbierto(false)
    },
  })

  const editarMutation = useMutation({
  mutationFn: ({ id, data }: { id: number; data: CategoriaCreate }) => {
    console.log("editarMutation ejecutando", id, data)
    return updateCategoria(id, data)
  },
  onSuccess: () => {
    console.log("editarMutation onSuccess")
    queryClient.invalidateQueries({ queryKey: ["categorias"] })
    setEditando(null)
  },
  onError: (error) => {
    console.log("editarMutation error", error)
  }
})
  const eliminarMutation = useMutation({
    mutationFn: deleteCategoria,
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ["categorias"] }),
  })

  const handleGuardar = (data: CategoriaCreate) => {
  console.log("handleGuardar llamado", data)
  console.log("editando", editando)
  if (editando) {
    editarMutation.mutate({ id: editando.id, data })
  } else {
    crearMutation.mutate(data)
  }
}

  if (isLoading) return <p className="p-8 text-gray-500">Cargando categorías...</p>
  if (isError) return <p className="p-8 text-red-500">Error al cargar categorías</p>

  return (
    <div className="p-8">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-gray-800">Categorías</h1>
        <button
          onClick={() => setModalAbierto(true)}
          className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
        >
          + Nueva Categoría
        </button>
      </div>

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
          {categorias.map((cat: Categoria) => (
            <tr key={cat.id} className="border-t hover:bg-gray-50">
              <td className="px-4 py-3 text-gray-800">{cat.id}</td>
              <td className="px-4 py-3 font-medium text-gray-800">{cat.nombre}</td>
              <td className="px-4 py-3 text-gray-500">{cat.descripcion}</td>
              <td className="px-4 py-3 text-gray-500">{cat.imagen_url}</td>
              <td className="px-4 py-3 flex gap-2">
                <button
                  onClick={() => setEditando(cat)}
                  className="bg-yellow-400 text-white px-3 py-1 rounded hover:bg-yellow-500 text-sm"
                >
                  Editar
                </button>
                <button
                  onClick={() => eliminarMutation.mutate(cat.id)}
                  className="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600 text-sm"
                >
                  Eliminar
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {modalAbierto && (
        <Modal
          titulo="Nueva Categoría"
          inicial={{ nombre: "", descripcion: "", imagen_url: "" }}
          onGuardar={handleGuardar}
          onCerrar={() => setModalAbierto(false)}
        />
      )}
      {editando && (
        <Modal
          titulo="Editar Categoría"
          inicial={{ nombre: editando.nombre, descripcion: editando.descripcion, imagen_url: editando.imagen_url ?? "" }}
          onGuardar={handleGuardar}
          onCerrar={() => setEditando(null)}
        />
      )}
    </div>
  )
}

export default CategoriasPage