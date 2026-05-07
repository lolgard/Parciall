import { useState } from "react"
import Modal from "../Modal"
import type { ProductoCreate } from "../../types/producto"
import type { Categoria } from "../../types/categoria"
import type { Ingrediente } from "../../types/ingredientes"

interface Props {
  titulo: string
  inicial: ProductoCreate
  categorias: Categoria[]
  ingredientes: Ingrediente[]
  onGuardar: (data: ProductoCreate) => void
  onCerrar: () => void
}

function ProductoModal({ titulo, inicial, categorias, ingredientes, onGuardar, onCerrar }: Props) {
  const [form, setForm] = useState<ProductoCreate>(inicial)

  const toggleIngrediente = (id: number) => {
    setForm((prev) => ({
      ...prev,
      ingredientes: prev.ingredientes.includes(id)
        ? prev.ingredientes.filter((i) => i !== id)
        : [...prev.ingredientes, id],
    }))
  }

  const handleGuardar = () => {
    if (form.categorias.length === 0) {
      alert("Debe seleccionar al menos una categoría")
      return
    }
    onGuardar(form)
  }

  return (
    <Modal titulo={titulo} onCerrar={onCerrar} onGuardar={handleGuardar}>
      <label className="text-sm font-medium text-gray-700">Nombre</label>
      <input
        className="border rounded-lg px-3 py-2"
        placeholder="Nombre"
        value={form.name}
        onChange={(e) => setForm({ ...form, name: e.target.value })}
      />
      <label className="text-sm font-medium text-gray-700">Precio</label>
      <input
        className="border rounded-lg px-3 py-2"
        type="number"
        placeholder="Precio"
        value={form.price === 0 ? "" : form.price}
        onChange={(e) => setForm({ ...form, price: Number(e.target.value) })}
      />
      <label className="text-sm font-medium text-gray-700">Stock</label>
      <input
        className="border rounded-lg px-3 py-2"
        type="number"
        placeholder="Stock"
        value={form.stock_cantidad === 0 ? "" : form.stock_cantidad}
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
    </Modal>
  )
}

export default ProductoModal
