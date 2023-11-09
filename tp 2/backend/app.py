from flask import Flask, jsonify, request
from flask_cors import CORS  # Esta librería permite habilitar CORS en Flask

app = Flask(__name__)
CORS(app)  # Habilita CORS para permitir peticiones desde un origen diferente al backend

# Lista de superhéroes y sus habilidades
servicios = [
    {"id":1,'nombre': 'Peluqueria', 'precio': 5000, "img":"https://koseiprofesional.com/wp-content/uploads/2017/06/tratamiento-de-keratina-peluqueria-scaled.jpg"},
    {"id":2,'nombre': 'Manicura', 'precio': 6000,  "img":"https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2023/01/24/16745628932796.jpg"},
    {"id":3,'nombre': 'Pedicura', 'precio': 4000, "img":"https://media.istockphoto.com/photos/pedicure-nail-filing-close-up-picture-id640018462?k=20&m=640018462&s=612x612&w=0&h=IS6HcBBR9qR2KMqhXEVR_PISAgxNKvsJoU26gdQVa1Y="},
    {"id":4,'nombre': 'Depilacion', 'precio': 5000, "img":"https://arc-anglerfish-arc2-prod-infobae.s3.amazonaws.com/public/364NW2QEYVCJJMLRDPY4F64YP4.jpg"},
    {"id":5,'nombre': 'Maquillaje', 'precio': 3500, "img":"https://unycos.com/blog/wp-content/uploads/2018/12/profesional-maquilla-a-joven.jpg"},
    {"id":6,'nombre': 'Spa', 'precio': 7000,"img":"https://img.freepik.com/foto-gratis/mujer-joven-masaje-facial-relajante-salon-spa_176420-7546.jpg?size=626&ext=jpg&ga=GA1.1.386372595.1698192000&semt=sph"}
]

# Ruta para obtener la lista de superhéroes y habilidades
@app.route('/servicios')
def get_servicios():
    return jsonify(servicios)

@app.route('/get/<int:id>')
def get(id):
    serviciosFound = [
        servicio for servicio in servicios if servicio['id'] == id]
    if (len(serviciosFound) > 0):
        return jsonify({'servicio': serviciosFound[0]})
    return jsonify({'message': 'Servicio no encontrado'})

@app.route('/add', methods=['POST'])
def add_servicio():
    new_servicio = {
        'id': request.json["id"],
        'nombre': request.json['nombre'],
        'precio': request.json['precio'],
        'img': request.json['img'],
    }
    servicios.append(new_servicio)
    return jsonify({"message":"Servicio agregado satisfactoriamente", 'services': servicios})

if __name__ == '__main__':
    app.run(debug=True)