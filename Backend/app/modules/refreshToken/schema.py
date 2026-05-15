from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel


class RefreshTokenRead(SQLModel):
    id: int
    token_hash: str

    expire_at : datetime
    revoked_at : Optional[datetime] = None
    created_at : datetime
    