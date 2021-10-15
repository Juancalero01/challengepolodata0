from conexion import DatosCategoria
db = DatosCategoria


class Categoria():
    def __init__(self):
        self.nombre = None

    def registrarCategoria(self, nombre):
        self.dato = db.datosCategoria()
        self.dato["categorias"].append(
            {
                "nombre": nombre,
            }
        )
        db.guardarCategoria(self.dato)

    def eliminarCategoria(self, nombre):
        self.dato = db.datosCategoria()
        for i in self.dato['categorias']:
            for v in i.values():
                if v == nombre:
                    self.dato["categorias"].remove(i)
        db.guardarCategoria(self.dato)

    def listarCategoria(self):
        self.dato = db.datosCategoria()
        print('NOMBRE')
        for i in self.dato['categorias']:
            for v in i.values():
                print(v, end=" ")
            print("\n==========")
