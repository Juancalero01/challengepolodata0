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
        self.contador = 0
        print('ID \t NOMBRE')
        for i in self.dato['categorias']:
            self.contador += 1
            print(f"{self.contador}", end=" ")
            for v in i.values():
                print(f"\t {v}", end=" ")
            print("\n===========================")

    def retornarCategoria(self, id):
        self.dato = db.datosCategoria()
        self.contador = 0
        for i in self.dato['categorias']:
            self.contador += 1
            if self.contador == id:
                for v in i.values():
                    return v
