import sqlite3

DATABASE_NAME = "servicios.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS servicios(
                id TEXT PRIMARY KEY,
                Servicios TEXT NOT NULL,
                Tipo TEXT NOT NULL,
                USD REAL NOT NULL
        )
        """
    ]

    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)

def seed_servicios():
    servicios = [
        "INSERT OR IGNORE INTO servicios (id, servicios, tipo, USD) VALUES ('R001', 'Peluqueria' , 'Corte de pelo', 4)",
        "INSERT OR IGNORE INTO servicios (id, servicios, tipo, USD) VALUES ('R002', 'Manicura' , 'Acrilica', 5)",
        "INSERT OR IGNORE INTO servicios (id, servicios, tipo, USD) VALUES ('R003', 'Manicura' , 'Semipermanente', 3)",
        "INSERT OR IGNORE INTO servicios (id, servicios, tipo, USD) VALUES ('R004', 'Pedicura' , 'semipermanente', 3)",
        "INSERT OR IGNORE INTO servicios (id, servicios, tipo, USD) VALUES ('R005', 'Depilación' , 'Con cera', 4)",
        "INSERT OR IGNORE INTO servicios (id, servicios, tipo, USD) VALUES ('R006', 'Peluqueria' , 'Tintura', 8)"
    ]

    db = get_db()
    cursor = db.cursor()
    for servicio in servicios:
        cursor.execute(servicio)
    db.commit()







