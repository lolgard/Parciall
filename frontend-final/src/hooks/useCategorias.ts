import { useState } from "react"
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query"
import { getCategorias, createCategoria, updateCategoria, deleteCategoria } from "../services/categoria.service"
import type { Categoria, CategoriaCreate } from "../types/categoria"

const INITIAL_FORM: CategoriaCreate = { nombre: "", descripcion: "", imagen_url: "" }

export function useCategorias() {
  const queryClient = useQueryClient()
  const [modalAbierto, setModalAbierto] = useState(false)
  const [editando, setEditando] = useState<Categoria | null>(null)

  const { data: categorias = [], isLoading, isError } = useQuery({
    queryKey: ["categorias"],
    queryFn: getCategorias,
  })

  const crearMutation = useMutation({
    mutationFn: createCategoria,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["categorias"] })
      setModalAbierto(false)
    },
  })

  const editarMutation = useMutation({
    mutationFn: ({ id, data }: { id: number; data: CategoriaCreate }) => updateCategoria(id, data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["categorias"] })
      setEditando(null)
    },
  })

  const eliminarMutation = useMutation({
    mutationFn: deleteCategoria,
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ["categorias"] }),
  })

  const handleGuardar = (data: CategoriaCreate) => {
    if (editando) {
      editarMutation.mutate({ id: editando.id, data })
    } else {
      crearMutation.mutate(data)
    }
  }

  return {
    categorias,
    isLoading,
    isError,
    modalAbierto,
    setModalAbierto,
    editando,
    setEditando,
    handleGuardar,
    eliminarMutation,
    INITIAL_FORM,
  }
}
