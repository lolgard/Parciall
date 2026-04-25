export interface Producto {
  id: number
  name: string
  price: number
  stock_cantidad: number
  disponible: boolean
}

export interface ProductoCreate {
  name: string
  price: number
  stock_cantidad: number
  disponible: boolean
  categorias: number[]
  ingredientes: number[]
}
export interface ProductoCategoria {
  categoria_id: number
  es_principal: boolean
}

export interface ProductoIngrediente {
  ingrediente_id: number
  cantidad: number
}

export interface Producto {
  id: number
  name: string
  price: number
  stock_cantidad: number
  disponible: boolean
  categorias: ProductoCategoria[]  // ← esto agregás
  ingredientes: ProductoIngrediente[]  // ← esto agregás
}