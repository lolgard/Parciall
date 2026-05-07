import { useIngredientes } from "../hooks/useIngredientes"
import IngredienteTable from "../components/ingredientes/IngredienteTable"
import IngredienteModal from "../components/ingredientes/IngredienteModal"
import PageHeader from "../components/PageHeader"
import { LoadingState } from "../components/FeedbackStates"

function IngredientesPage() {
  const {
    ingredientes, isLoading,
    modalAbierto, setModalAbierto,
    editando, setEditando,
    handleGuardar, eliminarMutation,
  } = useIngredientes()

  if (isLoading) return <LoadingState mensaje="Cargando ingredientes..." />

  return (
    <div className="p-8">
      <PageHeader titulo="Ingredientes" labelBoton="+ Nuevo Ingrediente" onNuevo={() => setModalAbierto(true)} />

      <IngredienteTable
        ingredientes={ingredientes}
        onEditar={setEditando}
        onEliminar={(id) => eliminarMutation.mutate(id)}
      />

      {modalAbierto && (
        <IngredienteModal
          titulo="Nuevo Ingrediente"
          inicial={{ name: "", description: "", esAlergeno: false }}
          onGuardar={handleGuardar}
          onCerrar={() => setModalAbierto(false)}
        />
      )}

      {editando && (
        <IngredienteModal
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
