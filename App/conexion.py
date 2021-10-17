import json

autor = 'App/Datos/autores.json'
categoria = 'App/Datos/categorias.json'
libro = 'App/Datos/libros.json'


class DatosAutor:
    def datosAutor():
        with open(autor, 'r') as archivo:
            datos = json.load(archivo)
        return datos

    def guardarAutor(dato):
        with open(autor, 'w') as archivo:
            json.dump(dato, archivo, indent=4)


class DatosCategoria:
    def datosCategoria():
        with open(categoria, 'r') as archivo:
            datos = json.load(archivo)
        return datos

    def guardarCategoria(dato):
        with open(categoria, 'w') as archivo:
            json.dump(dato, archivo, indent=4)


class DatosLibro:
    def datosLibro():
        with open(libro, 'r') as archivo:
            datos = json.load(archivo)
        return datos

    def guardarLibro(dato):
        with open(libro, 'w') as archivo:
            json.dump(dato, archivo, indent=4)
