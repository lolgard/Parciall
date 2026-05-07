import { useProductos } from "../hooks/useProductos"
import ProductoTable from "../components/productos/ProductoTable"
import ProductoModal from "../components/productos/ProductoModal"
import PageHeader from "../components/PageHeader"
import { LoadingState } from "../components/FeedbackStates"

function ProductoPage() {
  const {
    productos, categorias, ingredientes, isLoading,
    modalAbierto, setModalAbierto,
    editando, setEditando,
    handleGuardar, eliminarMutation,
  } = useProductos()

  if (isLoading) return <LoadingState mensaje="Cargando productos..." />

  return (
    <div className="p-8">
      <PageHeader titulo="Productos" labelBoton="+ Nuevo Producto" onNuevo={() => setModalAbierto(true)} />

      <ProductoTable
        productos={productos}
        categorias={categorias}
        ingredientes={ingredientes}
        onEditar={setEditando}
        onEliminar={(id) => eliminarMutation.mutate(id)}
      />

      {modalAbierto && (
        <ProductoModal
          titulo="Nuevo Producto"
          inicial={{ name: "", price: 0, stock_cantidad: 0, disponible: true, categorias: [], ingredientes: [] }}
          categorias={categorias}
          ingredientes={ingredientes}
          onGuardar={handleGuardar}
          onCerrar={() => setModalAbierto(false)}
        />
      )}

      {editando && (
        <ProductoModal
          titulo="Editar Producto"
          inicial={{
            name: editando.name,
            price: editando.price,
            stock_cantidad: editando.stock_cantidad,
            disponible: editando.disponible,
            categorias: [],
            ingredientes: [],
          }}
          categorias={categorias}
          ingredientes={ingredientes}
          onGuardar={handleGuardar}
          onCerrar={() => setEditando(null)}
        />
      )}
    </div>
  )
}

export default ProductoPage
