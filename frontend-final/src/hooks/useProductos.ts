import { useState } from "react"
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query"
import { getProductos, createProducto, updateProducto, deleteProducto } from "../services/producto.service"
import { getCategorias } from "../services/categoria.service"
import { getIngredientes } from "../services/ingrediente.service"
import type { Producto, ProductoCreate } from "../types/producto"

const INITIAL_FORM: ProductoCreate = {
  name: "",
  price: 0,
  stock_cantidad: 0,
  disponible: true,
  categorias: [],
  ingredientes: [],
}

export function useProductos() {
  const queryClient = useQueryClient()
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

  return {
    productos,
    categorias,
    ingredientes,
    isLoading,
    modalAbierto,
    setModalAbierto,
    editando,
    setEditando,
    handleGuardar,
    eliminarMutation,
    INITIAL_FORM,
  }
}
