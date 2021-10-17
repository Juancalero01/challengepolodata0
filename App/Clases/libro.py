from conexion import DatosLibro
db = DatosLibro


class Libro():
    def __init__(self):
        self.titulo = None
        self.autor = None
        self.categoria = None

    def registrarLibro(self, titulo, categoria, autor):
        self.dato = db.datosLibro()
        self.dato["libros"].append(
            {
                "titulo": titulo,
                "categoria": categoria,
                "autor": autor,
            }
        )
        db.guardarLibro(self.dato)

    def eliminarLibro(self, id):
        self.dato = db.datosLibro()
        self.contador = 0
        for i in self.dato['libros']:
            self.contador += 1
            if self.contador == id:
                self.dato['libros'].remove(i)
        db.guardarLibro(self.dato)

    def listarLibro(self):
        self.dato = db.datosLibro()
        self.contador = 0
        print("===========================")
        print('ID \t TITULO \t CATEGORIA \t AUTOR')
        print("===========================")
        for i in self.dato['libros']:
            self.contador += 1
            print(f"{self.contador}", end=" ")
            for v in i.values():
                print(f"\t {v}", end=" ")
            print("\n===========================")
