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
        self.contador = 0
        print('ID \t NOMBRE \t APELLIDO')
        for i in self.dato['autores']:
            self.contador += 1
            print(f"{self.contador}", end=" ")
            for v in i.values():
                print(f"\t {v}", end=" ")
            print("\n===========================")
