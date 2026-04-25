import { api } from "../api/axios"
import type{ IngredienteCreate } from "../types/ingredientes"

export const getIngredientes = async () => {
  const response = await api.get("/Ingredientes/")
  return response.data
}

export const createIngrediente = async (data: IngredienteCreate) => {
  const response = await api.post("/Ingredientes/", data)
  return response.data
}

export const updateIngrediente = async (id: number, data: IngredienteCreate) => {
  const response = await api.put(`/Ingredientes/${id}`, data)
  return response.data
}

export const deleteIngrediente = async (id: number) => {
  const response = await api.delete(`/Ingredientes/${id}`)
  return response.data
}