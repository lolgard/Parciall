import { api } from "../api/axios"
import type{ CategoriaCreate } from "../types/categoria"

export const getCategorias = async () => {
  const response = await api.get("/categorias/")
  return response.data
}

export const createCategoria = async (data: CategoriaCreate) => {
  const response = await api.post("/categorias/", data)
  return response.data
}

export const updateCategoria = async (id: number, data: CategoriaCreate) => {
  console.log("updateCategoria llamado", id, data)
  const response = await api.put(`/categorias/${id}`, data)
  console.log("updateCategoria respuesta", response.data)
  return response.data
}

export const deleteCategoria = async (id: number) => {
  const response = await api.delete(`/categorias/${id}`)
  return response.data
}