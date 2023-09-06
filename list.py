class List:
    def __init__(self, nombre, genero, temporadas, capitulos, estado):
        self.id = nombre.replace(" ","")
        self.nombre = nombre
        self.genero = genero
        self.temporadas = temporadas
        self.capitulos = capitulos
        self.estado = estado

#crea una estructura de la colección
    def toDBCollection(self):
        return{
            'id' : self.id,
            'nombre': self.nombre,
            'genero': self.genero,
            'temporadas': self.temporadas,
            'capitulos' : self.capitulos,
            'estado' : self.estado
        }