import { useState } from "react"
import Modal from "../Modal"
import type { IngredienteCreate } from "../../types/ingredientes"

interface Props {
  titulo: string
  inicial: IngredienteCreate
  onGuardar: (data: IngredienteCreate) => void
  onCerrar: () => void
}

function IngredienteModal({ titulo, inicial, onGuardar, onCerrar }: Props) {
  const [form, setForm] = useState<IngredienteCreate>(inicial)

  return (
    <Modal titulo={titulo} onCerrar={onCerrar} onGuardar={() => onGuardar(form)}>
      <label className="text-sm font-medium text-gray-700">Nombre</label>
      <input
        className="border rounded-lg px-3 py-2"
        placeholder="Nombre"
        value={form.name}
        onChange={(e) => setForm({ ...form, name: e.target.value })}
      />
      <label className="text-sm font-medium text-gray-700">Descripción</label>
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
    </Modal>
  )
}

export default IngredienteModal
