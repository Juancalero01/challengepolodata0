from conexion import DatosAutor
db = DatosAutor


class Autor():
    def __init__(self):
        self.nombre = None
        self.apellido = None

    def registrarAutor(self, nombre, apellido):
        self.dato = db.datosAutor()
        self.dato["autores"].append(
            {
                "nombre": nombre,
                "apellido": apellido
            }
        )
        db.guardarAutor(self.dato)

    def eliminarAutor(self, nombre):
        self.dato = db.datosAutor()
        for i in self.dato['autores']:
            for v in i.values():
                if v == nombre:
                    self.dato["autores"].remove(i)
        db.guardarAutor(self.dato)

    def listarAutor(self):
        self.dato = db.datosAutor()
        print('NOMBRE \t APELLIDO')
        for i in self.dato['autores']:
            for v in i.values():
                print(v, end=" \t ")
            print("\n=================================")
