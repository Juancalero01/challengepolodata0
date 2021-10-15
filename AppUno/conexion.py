import json
bd = 'categorias.json'


class BaseDatos():
    def leerBd():
        with open(bd, 'r') as archivo:
            datos = json.load(archivo)
        return datos

    def escribirBd(dato):
        with open(bd, 'w') as archivo:
            json.dump(dato, archivo, indent=4)
    