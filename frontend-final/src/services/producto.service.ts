import { api } from "../api/axios"
import type { ProductoCreate } from "../types/producto"

export const getProductos = async () => {
  const response = await api.get("/productos/")
  return response.data
}

export const getProductoById = async (id: number) => {
  const response = await api.get(`/productos/${id}`)
  return response.data
}

export const createProducto = async (data: ProductoCreate) => {
  const response = await api.post("/productos/", data)
  return response.data
}

export const updateProducto = async (id: number, data: ProductoCreate) => {
  const response = await api.put(`/productos/${id}`, data)
  return response.data
}

export const deleteProducto = async (id: number) => {
  const response = await api.delete(`/productos/${id}`)
  return response.data
}