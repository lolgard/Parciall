interface ModalProps {
  titulo: string
  onCerrar: () => void
  children: React.ReactNode
  onGuardar: () => void
}

function Modal({ titulo, onCerrar, children, onGuardar }: ModalProps) {
  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="bg-white rounded-xl p-6 w-full max-w-lg shadow-xl max-h-[90vh] overflow-y-auto">
        <h2 className="text-xl font-bold mb-4 text-gray-800">{titulo}</h2>
        <div className="flex flex-col gap-3">
          {children}
        </div>
        <div className="flex gap-2 mt-5 justify-end">
          <button
            onClick={onCerrar}
            className="px-4 py-2 rounded-lg border hover:bg-gray-100 text-gray-800"
          >
            Cancelar
          </button>
          <button
            onClick={onGuardar}
            className="px-4 py-2 rounded-lg bg-blue-600 text-white hover:bg-blue-700"
          >
            Guardar
          </button>
        </div>
      </div>
    </div>
  )
}

export default Modal
