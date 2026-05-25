import os
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está configurada en .env")

_is_sqlite = DATABASE_URL.startswith("sqlite")

if _is_sqlite:
    connect_args = {"check_same_thread": False}
    engine = create_engine(
        DATABASE_URL,
        echo=False,
        connect_args=connect_args,
    )
else:
    connect_args = {"sslmode": "require"}
    engine = create_engine(
        DATABASE_URL,
        echo=False,
        pool_pre_ping=True,
        connect_args=connect_args,
    )


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
