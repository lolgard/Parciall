interface Props {
  titulo: string
  labelBoton: string
  onNuevo: () => void
}

function PageHeader({ titulo, labelBoton, onNuevo }: Props) {
  return (
    <div className="flex justify-between items-center mb-6">
      <h1 className="text-3xl font-bold text-gray-800">{titulo}</h1>
      <button
        onClick={onNuevo}
        className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
      >
        {labelBoton}
      </button>
    </div>
  )
}

export default PageHeader
