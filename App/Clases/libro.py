from conexion import DatosLibro
db = DatosLibro


class Libro():
    def __init__(self):
        self.titulo = None
        self.autor = None
        self.categoria = None

    def registrarLibro(self, titulo, autor, categoria):
        self.dato = db.datosLibro()
        self.dato["libros"].append(
            {
                "titulo": titulo,
                "autor": autor,
                "categoria": categoria
            }
        )
        db.guardarLibro(self.dato)

    def eliminarLibro(self):
        pass    

    