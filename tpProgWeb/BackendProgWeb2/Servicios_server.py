from flask import Flask, jsonify, request
import controller_Servicios
from Servicios_db import create_tables, seed_servicios
from exhange import get_xr

app = Flask(__name__)


@app.route('/api/bellissima/articulos', methods=["GET"])
def get_rest():
    rest = controller_Servicios.get_servicios()
    rest_list = []
    for restr in rest:
        elem = restr.serialize()
        rest_list.append(elem)
    return jsonify(rest_list)


@app.route("/api/bellissima/articulos", methods=["POST"])
def insert_servicio():
    try:
        rest_detalles = request.get_json()
        id = rest_detalles["id"]
        servicios = rest_detalles["servicios"]
        tipo = rest_detalles["tipo"]
        USD = rest_detalles["USD"]
        result = controller_Servicios.insert_servicio(id, servicios, tipo, USD)
        return jsonify(result)
    except KeyError:
        return jsonify({'error': 'Missing or incorrect JSON keys in the request data'}), 400


@app.route("/api/bellissima/articulos", methods=["PUT"])
def update_servicio():
    serv_act = request.get_json()
    id = serv_act["id"]
    servicios = serv_act["servicios"]
    tipo = serv_act["tipo"]
    USD = serv_act["USD"]
    result = controller_Servicios.insert_servicio(USD, servicios, tipo, id)
    return jsonify(result)


@app.route("/api/bellissima/articulos/eliminate/<id>", methods=["DELETE"])
def delete_servicios(id):
    result = controller_Servicios.delete_servicio(id)
    return jsonify(result)


@app.route("/api/bellissima/articulos/<id>", methods=["GET"])
def get_by_id(id):
    try:
        rest = controller_Servicios.get_by_id(id)
        xr = get_xr()
        price_usd = rest['PESO'] * xr
        rest['PESO'] = round(price_usd, 2)
        return jsonify(rest)
    except:
        return jsonify({'error': 'Missing id parameter'}), 400


create_tables()
seed_servicios()
app.run()
