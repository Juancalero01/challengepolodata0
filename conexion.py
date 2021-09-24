import json


class ConexionJSON:
    def readJSON():
        with open("bdParteUno.json", "r") as archivo:
            dato = json.load(archivo)
        return dato

    def writeJSON(dato):
        with open("bdParteUno.json", "w") as archivo:
            json.dump(dato, archivo)
