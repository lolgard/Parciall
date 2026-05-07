import { useState } from "react"
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query"
import { getIngredientes, createIngrediente, updateIngrediente, deleteIngrediente } from "../services/ingrediente.service"
import type { Ingrediente, IngredienteCreate } from "../types/ingredientes"

const INITIAL_FORM: IngredienteCreate = { name: "", description: "", esAlergeno: false }

export function useIngredientes() {
  const queryClient = useQueryClient()
  const [modalAbierto, setModalAbierto] = useState(false)
  const [editando, setEditando] = useState<Ingrediente | null>(null)

  const { data: ingredientes = [], isLoading, isError } = useQuery({
    queryKey: ["ingredientes"],
    queryFn: getIngredientes,
  })

  const crearMutation = useMutation({
    mutationFn: createIngrediente,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["ingredientes"] })
      setModalAbierto(false)
    },
  })

  const editarMutation = useMutation({
    mutationFn: ({ id, data }: { id: number; data: IngredienteCreate }) => updateIngrediente(id, data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["ingredientes"] })
      setEditando(null)
    },
  })

  const eliminarMutation = useMutation({
    mutationFn: deleteIngrediente,
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ["ingredientes"] }),
  })

  const handleGuardar = (data: IngredienteCreate) => {
    if (editando) {
      editarMutation.mutate({ id: editando.id, data })
    } else {
      crearMutation.mutate(data)
    }
  }

  return {
    ingredientes,
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
