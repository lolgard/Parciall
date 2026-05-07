export function LoadingState({ mensaje = "Cargando..." }: { mensaje?: string }) {
  return <p className="p-8 text-gray-500">{mensaje}</p>
}

export function ErrorState({ mensaje = "Ocurrió un error" }: { mensaje?: string }) {
  return <p className="p-8 text-red-500">{mensaje}</p>
}
