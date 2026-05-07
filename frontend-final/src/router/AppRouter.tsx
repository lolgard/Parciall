import '../App.css'
import { BrowserRouter, Route, Routes } from 'react-router-dom'

import ProductDetailPage from '../pages/ProductDetailPage'
import CategoriasPage from '../pages/Categorias.Page'
import IngredientesPage from '../pages/Ingredientes.Page'
import ProductoPage from '../pages/ProductoPage'

import Navbar from '../components/Navbar'

function AppRouter() {
  return (
    <BrowserRouter>
      <Navbar />

      <Routes>
        <Route path="/" element={<ProductoPage />} />
        <Route path="/categorias" element={<CategoriasPage />} />
        <Route path="/ingredientes" element={<IngredientesPage />} />
        <Route path="/productos" element={<ProductoPage />} />
        <Route path="/productos/:id" element={<ProductDetailPage />} />
      </Routes>
    </BrowserRouter>
  )
}

export default AppRouter