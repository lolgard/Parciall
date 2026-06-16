readme1.md
from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None

    readme1.md
from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None

    readme1.md
from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None

    readme1.md
from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None

    readme1.md
from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None

    readme1.md
from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None

    readme1.md
from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None

    readme1.md
from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None

    readme1.md
from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
readme1.md
from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel
from app.modules.rol.schema import RolRead
class UsuarioBase(SQLModel):
    email: str
    name: str
    lastname: str
    phone_number: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password_hash: str
    roles: Optional[list[str]] = None

class UsuarioRead(UsuarioBase):
    id: int
    deleted_at: Optional[datetime] = None
    roles: list[str] = []

class UsuarioDetallesRead(UsuarioRead):
    direccionEntrega: list[str] = []


class UsuarioRolRead(SQLModel):
    roles: list[RolRead] = []
    usuario_id: Optional[int] = None
    asignado_por_id: Optional[int] = None


class UsuarioUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[int] = None
    password_hash: Optional[str] = None
    roles: Optional[list[str]] = None
    activo: Optional[bool] = None
    
    
