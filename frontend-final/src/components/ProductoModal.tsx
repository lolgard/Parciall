import { useState } from "react";
export const ProductoModal = ({
  open,
  onClose,
  onSubmit,
  producto,
}: any) => {
  const [form, setForm] = useState({
    name: "",
    price: 0,
    stock_cantidad: 0,
    categorias: [],
    ingredientes: [],
  });

  const handleChange = (e: any) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  if (!open) return null;

  return (
    <div className="modal">
      <input name="name" onChange={handleChange} placeholder="Nombre" />
      <input name="price" onChange={handleChange} />
      <input name="stock_cantidad" onChange={handleChange} />

      <button onClick={() => onSubmit(form)}>
        Guardar
      </button>
    </div>
  );
};
