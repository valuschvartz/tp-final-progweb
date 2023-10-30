from flask import Flask, render_template, request

app = Flask(__name__, static_folder='.', static_url_path='')

# Lista para almacenar los datos
datos = []

@app.route('/')
def formulario():
    return render_template('/FrontEdnProgWeb/simulador/contacto.html')

@app.route('/guardar_datos', methods=['POST'])
def guardar_datos():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    email = request.form['email']
    mensaje = request.form['message']

    # Guardar los datos en la lista
    datos.append({'nombre': nombre, 'apellido': apellido, 'email': email, 'mensaje': mensaje})

    return 'Datos guardados correctamente.'

@app.route('/otra_pagina')
def otra_pagina():
    return render_template('otra_pagina.html')

if __name__ == '__main__':
    app.run(debug=True)
