import { useState } from "react"
import Modal from "../Modal"
import type { CategoriaCreate } from "../../types/categoria"

interface Props {
  titulo: string
  inicial: CategoriaCreate
  onGuardar: (data: CategoriaCreate) => void
  onCerrar: () => void
}

function CategoriaModal({ titulo, inicial, onGuardar, onCerrar }: Props) {
  const [form, setForm] = useState<CategoriaCreate>(inicial)

  return (
    <Modal titulo={titulo} onCerrar={onCerrar} onGuardar={() => onGuardar(form)}>
      <label className="text-sm font-medium text-gray-700">Nombre</label>
      <input
        className="border rounded-lg px-3 py-2 text-gray-800"
        placeholder="Nombre"
        value={form.nombre}
        onChange={(e) => setForm({ ...form, nombre: e.target.value })}
      />
      <label className="text-sm font-medium text-gray-700">Descripción</label>
      <input
        className="border rounded-lg px-3 py-2 text-gray-800"
        placeholder="Descripción"
        value={form.descripcion}
        onChange={(e) => setForm({ ...form, descripcion: e.target.value })}
      />
      <label className="text-sm font-medium text-gray-700">URL de imagen</label>
      <input
        className="border rounded-lg px-3 py-2 text-gray-800"
        placeholder="URL de imagen"
        value={form.imagen_url}
        onChange={(e) => setForm({ ...form, imagen_url: e.target.value })}
      />
    </Modal>
  )
}

export default CategoriaModal
