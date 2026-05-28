from sqlalchemy import text, inspect


def run_migrations(engine):
    """Aplica migraciones incrementales a la DB. Idempotente."""
    # Usamos el inspector de SQLAlchemy que funciona tanto en SQLite como en PostgreSQL
    inspector = inspect(engine)
    
    # Migración para la tabla 'producto' (agregar imagen_url si falta)
    if "producto" in inspector.get_table_names():
        prod_cols = {col["name"] for col in inspector.get_columns("producto")}
        if "imagen_url" not in prod_cols:
            with engine.connect() as conn:
                conn.execute(text("ALTER TABLE producto ADD COLUMN imagen_url VARCHAR"))
                conn.commit()

    # Si la tabla 'pedido' no existe todavía, SQLModel la creará en startup
    if "pedido" not in inspector.get_table_names():
        return

    # Obtenemos las columnas actuales de la tabla 'pedido'
    cols = {col["name"] for col in inspector.get_columns("pedido")}

    with engine.connect() as conn:
        is_sqlite = engine.url.drivername.startswith("sqlite")

        if "nombre_cliente" not in cols:
            if is_sqlite:
                # En SQLite recreamos la tabla ya que no soporta ALTER TABLE complejo
                _recreate_pedido_table(conn)
            else:
                # En PostgreSQL agregamos las columnas directamente de forma segura
                for col, col_type in [
                    ("ip_cliente", "TEXT"),
                    ("extra_data", "TEXT"),
                    ("nombre_cliente", "VARCHAR"),
                    ("telefono", "VARCHAR"),
                ]:
                    if col not in cols:
                        conn.execute(text(f"ALTER TABLE pedido ADD COLUMN IF NOT EXISTS {col} {col_type}"))
        else:
            # Solo agregar columnas que falten
            for col, col_type in [
                ("ip_cliente", "TEXT"),
                ("extra_data", "TEXT"),
                ("nombre_cliente", "VARCHAR"),
                ("telefono", "VARCHAR"),
            ]:
                if col not in cols:
                    conn.execute(text(f"ALTER TABLE pedido ADD COLUMN {col} {col_type}"))

        conn.commit()


def _recreate_pedido_table(conn):
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS pedido_new (
            id          INTEGER PRIMARY KEY,
            usuario_id  INTEGER REFERENCES usuario(id),
            direccion_entrega_id INTEGER REFERENCES direccionentrega(id),
            estado_codigo    VARCHAR NOT NULL DEFAULT 'none',
            forma_pago_codigo VARCHAR NOT NULL DEFAULT 'none',
            subtotal    FLOAT NOT NULL,
            descuento   FLOAT NOT NULL DEFAULT 0.0,
            costo_envio FLOAT NOT NULL DEFAULT 0.0,
            total       FLOAT NOT NULL,
            notas       VARCHAR,
            nombre_cliente VARCHAR,
            telefono    VARCHAR,
            ip_cliente  TEXT,
            extra_data  TEXT,
            created_at  DATETIME,
            updated_at  DATETIME,
            deleted_at  DATETIME
        )
    """))

    conn.execute(text("""
        INSERT INTO pedido_new
            (id, usuario_id, direccion_entrega_id, estado_codigo, forma_pago_codigo,
             subtotal, descuento, costo_envio, total, notas,
             nombre_cliente, telefono, ip_cliente, extra_data,
             created_at, updated_at, deleted_at)
        SELECT
            id, usuario_id, direccion_entrega_id, estado_codigo, forma_pago_codigo,
            subtotal, descuento, costo_envio, total, notas,
            NULL, NULL, NULL, NULL,
            created_at, updated_at, deleted_at
        FROM pedido
    """))

    conn.execute(text("DROP TABLE pedido"))
    conn.execute(text("ALTER TABLE pedido_new RENAME TO pedido"))
