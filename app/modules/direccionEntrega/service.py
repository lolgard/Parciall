from fastapi import HTTPException

from app.modules.direccionEntrega.unit_of_work import DireccionEntregaUnitOfWork
from app.modules.direccionEntrega.model import DireccionEntrega
from app.modules.direccionEntrega.schema import DireccionEntregaCreate, DireccionEntregaUpdate
from app.modules.usuario.model import Usuario
from app.modules.usuario.schema import UsuarioRead


class DireccionEntregaService:
    def __init__(self, uow: DireccionEntregaUnitOfWork):
        self.uow = uow

    def direccion_service_create(self, data: DireccionEntregaCreate):
        with self.uow as uow:
            # validar usuario si viene
            if data.usuario_id:
                usuario = uow.usuarios.get_by_id(data.usuario_id)
                if not usuario:
                    raise HTTPException(404, "Usuario no encontrado")
                
                # Validar límite máximo de 3 direcciones activas
                direcciones_activas = [d for d in uow.direccion_entregas.get_all() if d.usuario_id == data.usuario_id]
                if len(direcciones_activas) >= 3:
                    raise HTTPException(400, "Límite máximo de 3 direcciones alcanzado.")

            direccion = DireccionEntrega(**data.dict())
            return uow.direccion_entregas.add(direccion)

    def get_all(self, current_user: UsuarioRead, usuario_id: int = None, all_addresses: bool = False):
        with self.uow as uow:
            Direcciones = uow.direccion_entregas.get_all()
            if not Direcciones:
                return []
            
            if all_addresses:
                if "ADMIN" not in current_user.roles:
                    raise HTTPException(403, "Solo un ADMIN puede ver todas las direcciones")
                return Direcciones
                
            target_id = current_user.id
            if usuario_id is not None:
                if "ADMIN" not in current_user.roles and current_user.id != usuario_id:
                    raise HTTPException(403, "No tienes permisos para ver direcciones de otros usuarios")
                target_id = usuario_id
                
            return [d for d in Direcciones if d.usuario_id == target_id]

    def get_by_id(self, direccion_id: int, current_user: UsuarioRead):
        with self.uow as uow:
            direccion = uow.direccion_entregas.get_by_id(direccion_id)
            if not direccion:
                raise HTTPException(404, "Dirección no encontrada")
            if "ADMIN" not in current_user.roles and direccion.usuario_id != current_user.id:
                raise HTTPException(403, "Acceso denegado a esta dirección")
            return direccion

    def update(self, direccion_id: int, data: DireccionEntregaUpdate, current_user: UsuarioRead):
        with self.uow as uow:
            direccion_vieja = uow.direccion_entregas.get_by_id(direccion_id)
            if not direccion_vieja:
                raise HTTPException(404, "Dirección no encontrada")
            if "ADMIN" not in current_user.roles and direccion_vieja.usuario_id != current_user.id:
                raise HTTPException(403, "No tienes permisos para modificar esta dirección")

            # Crear una nueva dirección con los datos viejos + los cambios (para no afectar pedidos históricos)
            datos_nueva = direccion_vieja.dict(exclude={'id', 'created_at', 'updated_at', 'deleted_at'})
            datos_nuevos_recibidos = data.dict(exclude_unset=True)
            datos_nueva.update(datos_nuevos_recibidos)

            nueva_direccion = DireccionEntrega(**datos_nueva)
            uow.direccion_entregas.add(nueva_direccion)

            # Hacer Soft Delete de la dirección vieja
            uow.direccion_entregas.delete(direccion_vieja)

            return nueva_direccion

    def delete(self, direccion_id: int, current_user: UsuarioRead):
        with self.uow as uow:
            direccion = uow.direccion_entregas.get_by_id(direccion_id)
            if not direccion:
                raise HTTPException(404, "Dirección no encontrada")
            if "ADMIN" not in current_user.roles and direccion.usuario_id != current_user.id:
                raise HTTPException(403, "No tienes permisos para eliminar esta dirección")
            uow.direccion_entregas.delete(direccion)
