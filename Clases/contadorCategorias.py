class Contador():
    def __init__(self, inicio=0):
        self.numero = inicio

    def contar(self):
        self.numero += 1
        return self.numero
