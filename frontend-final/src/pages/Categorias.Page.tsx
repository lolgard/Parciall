import { useCategorias } from "../hooks/useCategorias"
import CategoriaTable from "../components/categorias/CategoriaTable"
import CategoriaModal from "../components/categorias/CategoriaModal"
import PageHeader from "../components/PageHeader"
import { LoadingState, ErrorState } from "../components/FeedbackStates"

function CategoriasPage() {
  const {
    categorias, isLoading, isError,
    modalAbierto, setModalAbierto,
    editando, setEditando,
    handleGuardar, eliminarMutation,
  } = useCategorias()

  if (isLoading) return <LoadingState mensaje="Cargando categorías..." />
  if (isError) return <ErrorState mensaje="Error al cargar categorías" />

  return (
    <div className="p-8">
      <PageHeader titulo="Categorías" labelBoton="+ Nueva Categoría" onNuevo={() => setModalAbierto(true)} />

      <CategoriaTable
        categorias={categorias}
        onEditar={setEditando}
        onEliminar={(id) => eliminarMutation.mutate(id)}
      />

      {modalAbierto && (
        <CategoriaModal
          titulo="Nueva Categoría"
          inicial={{ nombre: "", descripcion: "", imagen_url: "" }}
          onGuardar={handleGuardar}
          onCerrar={() => setModalAbierto(false)}
        />
      )}

      {editando && (
        <CategoriaModal
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
