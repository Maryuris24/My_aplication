from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://melisahuete:a1n2i3m4e5@app.m76bbob.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()
#mongodb+srv://Admin:admin1@cluster0.pchtjug.mongodb.net/?retryWrites=true&w=majority

# definimos el método de conexión
def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["Agenda_db_animes"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db
