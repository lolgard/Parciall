import { useState } from "react"
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query"
import { useNavigate } from "react-router-dom"
import { getProductos, createProducto, updateProducto, deleteProducto } from "../services/producto.service"
import { getCategorias } from "../services/categoria.service"
import { getIngredientes } from "../services/ingrediente.service"
import type{ Producto, ProductoCreate } from "../types/producto"
import type{ Categoria } from "../types/categoria"
import type{ Ingrediente } from "../types/ingredientes"

interface ModalProps {
  inicial: ProductoCreate
  onGuardar: (data: ProductoCreate) => void
  onCerrar: () => void
  titulo: string
  categorias: Categoria[]
  ingredientes: Ingrediente[]
}

function Modal({ inicial, onGuardar, onCerrar, titulo, categorias, ingredientes }: ModalProps) {
  const [form, setForm] = useState<ProductoCreate>(inicial)

  const toggleCategoria = (id: number) => {
    setForm((prev) => ({
      ...prev,
      categorias: prev.categorias.includes(id)
        ? prev.categorias.filter((c) => c !== id)
        : [...prev.categorias, id],
    }))
  }

  const toggleIngrediente = (id: number) => {
    setForm((prev) => ({
      ...prev,
      ingredientes: prev.ingredientes.includes(id)
        ? prev.ingredientes.filter((i) => i !== id)
        : [...prev.ingredientes, id],
    }))
  }

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="bg-white rounded-xl p-6 w-full max-w-lg shadow-xl max-h-[90vh] overflow-y-auto">
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
            type="number"
            placeholder="Precio"
            value={form.price}
            onChange={(e) => setForm({ ...form, price: Number(e.target.value) })}
          />
          <input
            className="border rounded-lg px-3 py-2"
            type="number"
            placeholder="Stock"
            value={form.stock_cantidad}
            onChange={(e) => setForm({ ...form, stock_cantidad: Number(e.target.value) })}
          />
          <label className="flex items-center gap-2 cursor-pointer">
            <input
              type="checkbox"
              checked={form.disponible}
              onChange={(e) => setForm({ ...form, disponible: e.target.checked })}
            />
            <span>Disponible</span>
          </label>

          <div>
            <p className="font-semibold mb-1">Categorías:</p>
            <div className="flex flex-wrap gap-2">
              {categorias.map((cat) => (
                <label key={cat.id} className="flex items-center gap-1 cursor-pointer">
                  <input
                    type="radio"
                    name="categoria"
                    checked={form.categorias.includes(cat.id)}
                    onChange={() => setForm({ ...form, categorias: [cat.id] })}
                  />
                  <span className="text-sm">{cat.nombre}</span>
                </label>
              ))}
            </div>
          </div>

          <div>
            <p className="font-semibold mb-1">Ingredientes:</p>
            <div className="flex flex-wrap gap-2">
              {ingredientes.map((ing) => (
                <label key={ing.id} className="flex items-center gap-1 cursor-pointer">
                  <input
                    type="checkbox"
                    checked={form.ingredientes.includes(ing.id)}
                    onChange={() => toggleIngrediente(ing.id)}
                  />
                  <span className="text-sm">{ing.name}</span>
                </label>
              ))}
            </div>
          </div>
        </div>
        <div className="flex gap-2 mt-5 justify-end">
          <button onClick={onCerrar} className="px-4 py-2 rounded-lg border hover:bg-gray-100">Cancelar</button>
          <button
            onClick={() => {
              if (form.categorias.length === 0) {
                alert("Debe seleccionar al menos una categoría")
                return
              }
              onGuardar(form)
            }}
            className="px-4 py-2 rounded-lg bg-blue-600 text-white hover:bg-blue-700"
          >
            Guardar
          </button>
        </div>
      </div>
    </div>
  )
}

function ProductoPage() {
  const queryClient = useQueryClient()
  const navigate = useNavigate()
  const [modalAbierto, setModalAbierto] = useState(false)
  const [editando, setEditando] = useState<Producto | null>(null)

  const { data: productos = [], isLoading } = useQuery({
    queryKey: ["productos"],
    queryFn: getProductos,
  })

  const { data: categorias = [] } = useQuery({
    queryKey: ["categorias"],
    queryFn: getCategorias,
  })

  const { data: ingredientes = [] } = useQuery({
    queryKey: ["ingredientes"],
    queryFn: getIngredientes,
  })

  const crearMutation = useMutation({
    mutationFn: createProducto,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["productos"] })
      setModalAbierto(false)
    },
  })

  const editarMutation = useMutation({
    mutationFn: ({ id, data }: { id: number; data: ProductoCreate }) => updateProducto(id, data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["productos"] })
      setEditando(null)
    },
  })

  const eliminarMutation = useMutation({
    mutationFn: deleteProducto,
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ["productos"] }),
  })

  const handleGuardar = (data: ProductoCreate) => {
    if (editando) {
      editarMutation.mutate({ id: editando.id, data })
    } else {
      crearMutation.mutate(data)
    }
  }

  if (isLoading) return <p className="p-8 text-gray-500">Cargando productos...</p>

  return (
    <div className="p-8">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-gray-800">Productos</h1>
        <button
          onClick={() => setModalAbierto(true)}
          className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
        >
          + Nuevo Producto
        </button>
      </div>

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
            productos.map((prod: Producto) => (
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
                  {prod.categorias?.map(c =>
                    categorias.find((cat: Categoria) => cat.id === c.categoria_id)?.nombre
                  ).join(", ")}
                </td>
                <td className="px-4 py-3">
                  {prod.ingredientes?.map(i =>
                    ingredientes.find((ing: Ingrediente) => ing.id === i.ingrediente_id)?.name
                  ).join(", ")}
                </td>
                <td className="px-4 py-3 flex gap-2">
                  <button
                    onClick={() => navigate(`/productos/${prod.id}`)}
                    className="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600 text-sm"
                  >
                    Ver
                  </button>
                  <button
                    onClick={() => setEditando(prod)}
                    className="bg-yellow-400 text-white px-3 py-1 rounded hover:bg-yellow-500 text-sm"
                  >
                    Editar
                  </button>
                  <button
                    onClick={() => eliminarMutation.mutate(prod.id)}
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
          titulo="Nuevo Producto"
          inicial={{ name: "", price: 0, stock_cantidad: 0, disponible: true, categorias: [], ingredientes: [] }}
          onGuardar={handleGuardar}
          onCerrar={() => setModalAbierto(false)}
          categorias={categorias}
          ingredientes={ingredientes}
        />
      )}
      {editando && (
        <Modal
          titulo="Editar Producto"
          inicial={{ name: editando.name, price: editando.price, stock_cantidad: editando.stock_cantidad, disponible: editando.disponible, categorias: [], ingredientes: [] }}
          onGuardar={handleGuardar}
          onCerrar={() => setEditando(null)}
          categorias={categorias}
          ingredientes={ingredientes}
        />
      )}
    </div>
  )
}

export default ProductoPage