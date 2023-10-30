from Servicios_db import get_db
from clase_Servicios import Servicios


def get_servicios():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, servicios, tipo, USD FROM servicios"
    cursor.execute(query)
    servicio_list = cursor.fetchall()
    list_of_servicios = []
    for servicio in servicio_list:
        id = servicio[0]
        servicios = servicio[1]
        tipo = servicio[2]
        USD = servicio[3]
        servicio_to_add = Servicios(id, servicios, tipo, USD)
        list_of_servicios.append(servicio_to_add)
    return list_of_servicios


def insert_servicio(id, servicios, tipo, USD):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO Servicios(id, servicios, tipo, USD) VALUES " \
                "( ?, ?, ?, ?)"
    cursor.execute(statement, [id, servicios, tipo, USD])
    db.commit()
    return True


def update_servicio(id, servicios, tipo, USD):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE servicios SET servicios = ?, tipo = ?, USD= ? \
    WHERE id = ?"
    cursor.execute(statement, [id, servicios, tipo, USD])
    db.commit()
    return True


def delete_servicio(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM servicios WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, Servicios, Marca, USD FROM [servicios] WHERE id = ?"
    cursor.execute(statement, [id])
    single_servicio = cursor.fetchone()
    id = single_servicio[0]
    servicios = single_servicio[1]
    tipo = single_servicio[2]
    USD = single_servicio[3]
    rest = Servicios(id, servicios, tipo, USD)
    return rest.serialize_arg()
