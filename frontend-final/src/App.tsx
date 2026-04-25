import './App.css'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import ProductDetailPage from './pages/productDetailPage'
import CategoriasPage from './pages/categoria.page'
import IngredientesPage from './pages/ingredientes.page'
import ProductoPage from './pages/productoPage'
import Navbar from './components/Navbar'
function App() {

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

export default App
