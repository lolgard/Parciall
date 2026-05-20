from fastapi import HTTPException
from sqlmodel import select

from app.modules.usuario.unit_of_work import UsuarioUnitOfWork
from app.modules.usuario.model import Usuario
from app.modules.usuario.schema import UsuarioCreate, UsuarioUpdate
from app.core.security import hash_password


class UsuarioService:
    def __init__(self, session):
        self._session = session

    def usuario_service_create(self, data: UsuarioCreate):
        with UsuarioUnitOfWork(self._session) as uow:
            if not data.name or not data.name.strip():
                raise HTTPException(400, "El nombre no puede estar vacío")

            # email único
            existente = self._session.exec(
                select(Usuario).where(Usuario.email == data.email)
            ).first()
            if existente:
                raise HTTPException(400, "Ya existe un usuario con ese email")

            # hashear contraseña
            if not data.password_hash:
                raise HTTPException(400, "La contraseña es obligatoria")

            data.password_hash = hash_password(data.password_hash)

            # crear y persistir directamente en la sesión para evitar inconsistencias
            usuario = Usuario(**data.dict(exclude={"roles"}))
            uow._session.add(usuario)
            uow._session.flush()
            uow._session.refresh(usuario)
            return usuario

    def get_all(self):
        with UsuarioUnitOfWork(self._session) as uow:
            usuarios = uow.usuarios.get_all()
            if not usuarios:
                raise HTTPException(404, "No se encontraron usuarios")
            return usuarios

    def get_by_id(self, usuario_id: int):
        with UsuarioUnitOfWork(self._session) as uow:
            usuario = uow.usuarios.get_by_id(usuario_id)
            if not usuario:
                raise HTTPException(404, "Usuario no encontrado")
            return usuario

    def update(self, usuario_id: int, data: UsuarioUpdate):
        with UsuarioUnitOfWork(self._session) as uow:
            usuario = uow.usuarios.get_by_id(usuario_id)
            if not usuario:
                raise HTTPException(404, "Usuario no encontrado")

            if data.name is not None:
                usuario.name = data.name
            if data.lastname is not None:
                usuario.lastname = data.lastname
            if data.email is not None:
                usuario.email = data.email
            if data.phone_number is not None:
                usuario.phone_number = data.phone_number
            if data.password_hash:
                usuario.password_hash = hash_password(data.password_hash)

            uow.usuarios.update(usuario)
            uow._session.refresh(usuario)
            return usuario

    def delete(self, usuario_id: int):
        with UsuarioUnitOfWork(self._session) as uow:
            usuario = uow.usuarios.get_by_id(usuario_id)
            if not usuario:
                raise HTTPException(404, "Usuario no encontrado")
            uow.usuarios.delete(usuario)
