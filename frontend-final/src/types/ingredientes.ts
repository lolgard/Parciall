export interface Ingrediente {
  id: number
  name: string
  description: string
  esAlergeno: boolean
}

export interface IngredienteCreate {
  name: string
  description: string
  esAlergeno: boolean
}