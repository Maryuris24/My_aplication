from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import models as dbase
from list import List

db = dbase.dbConnection()
app=Flask(__name__)

# Desplega los datos de la colección
@app.route('/')
def inicio():
    listado = db['listado']
    listadoReceived = listado.find()
    return render_template('index.html', listado = listadoReceived)

#agregar
@app.route('/listado', methods=['POST'])
def addList():

    listado = db['listado']
    nombre = request.form['nombre']
    genero = request.form['genero']
    temporadas = request.form['temporadas']
    capitulos = request.form['capitulos']
    estado = request.form['estado']

    if nombre and genero and temporadas and capitulos and estado:

        list = List(nombre, genero, temporadas, capitulos, estado)
        listado.insert_one(list.toDBCollection())

        response = jsonify({
            'nombre': nombre,
            'genero': genero,
            'temporadas': temporadas,
            'capitulos' : capitulos,
            'estado' : estado
        })

        return redirect(url_for('inicio'))
    else:
        return notFound()   

#editar

@app.route('/editar/<string:list_name>', methods=['POST'])
def edit(list_name):

    listado = db['listado']
    nombre = request.form['nombre']
    genero = request.form['genero']
    temporadas = request.form['temporadas']
    capitulos = request.form['capitulos']
    estado = request.form['estado']

    if nombre and genero and temporadas and capitulos and estado:

        listado.update_one(
            {'id' : list_name},
                {'$set' : {
                    'nombre': nombre,
                    'genero': genero,
                    'temporadas': temporadas,
                    'capitulos' : capitulos,
                    'estado' : estado
                }})
        
        response = jsonify({
            'message' : list_name + 'actualizado corectamente'
        })

        return redirect(url_for('inicio'))
    else:
        return notFound()

#borrar
@app.route('/delete/<string:list_name>')
def delete(list_name):
    listado = db['listado']
    listado.delete_one({'id' : list_name})
    return redirect(url_for('inicio'))

#Método de error
@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)