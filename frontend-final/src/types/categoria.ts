export interface Categoria {
  id: number
  nombre: string
  descripcion: string
  imagen_url: string
}

export interface CategoriaCreate {
  nombre: string
  descripcion: string
  imagen_url: string
}