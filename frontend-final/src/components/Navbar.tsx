import { Link } from "react-router-dom"

function Navbar() {
  return (
    <nav className="bg-gray-800 text-white px-8 py-4 flex gap-6">
      <Link to="/productos" className="hover:text-blue-400">Productos</Link>
      <Link to="/categorias" className="hover:text-blue-400">Categorías</Link>
      <Link to="/ingredientes" className="hover:text-blue-400">Ingredientes</Link>
    </nav>
  )
}

export default Navbar