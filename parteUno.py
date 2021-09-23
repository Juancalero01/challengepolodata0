# import json
import os
os.system('cls')

# Desarrollar un programa que sea capaz de gestionar un listado de categorías de libros, esto implica poder agregar y eliminar elementos
# a partir de la interacción con el usuario.

# Se deberá poner en práctica el concepto de persistencia de datos en archivos, permitiendo continuar
# trabajando si el programa termina y luego lo volvemos a ejecutar.

# Se deberán utilizar clases para definir la estructura de los datos, en este caso, Categoria. Los atributos y métodos a utilizar son de libre elección.


class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre


def agregarCategoria():
    nombre = input('INGRESE UN NOMBRE PARA LA CATEGORIA: ')
    categoria = Categoria(nombre)
    print(categoria.nombre)
    pass


def eliminarCategoria():
    pass


while True:
    agregarCategoria()
    print('[1] AGREGAR CATEGORIA')
    print('[2] ELIMINAR CATEGORIA')
    print('[3] LISTAR CATEGORIA')
    print('[4] SALIR DEL PROGRAMA')
    op = int(input('INGRESE LA OPCION: '))
    if op == 1:
        pass
    elif op == 2:
        pass
    elif op == 3:
        pass
    elif op == 4:
        exit()
