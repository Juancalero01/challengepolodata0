
import os
from conexion import ConexionJSON
os.system('cls')

# Desarrollar un programa que sea capaz de gestionar un listado de categorías de libros, esto implica poder agregar y eliminar elementos
# a partir de la interacción con el usuario.

# Se deberá poner en práctica el concepto de persistencia de datos en archivos, permitiendo continuar
# trabajando si el programa termina y luego lo volvemos a ejecutar.

# Se deberán utilizar clases para definir la estructura de los datos, en este caso, Categoria. Los atributos y métodos a utilizar son de libre elección.


conn = ConexionJSON


class Categoria:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion


def addCategory():
    # dato = {}
    # dato["Categorias"] = []
    nombre = input('INGRESE UN NOMBRE PARA LA CATEGORIA: ')
    descripcion = input('INGRESE UNA DESCRIPCION BREVE DE LA CATEGORIA: ')
    categoria = Categoria(nombre, descripcion)
    dato = conn.readJSON()
    dato["Categorias"].append(
        {
            "nombre": categoria.nombre,
            "descripcion": categoria.descripcion
        }
    )
    conn.writeJSON(dato)


def removeCategory():
    dato = conn.readJSON()
    nombreCategoria = input("INGRESE EL NOMBRE DE LA CATEGORIA A ELIMINAR: ")
    for i in dato["Categorias"]:
        for value in i.values():
            if value == nombreCategoria:
                dato["Categorias"].remove(i)
    conn.writeJSON(dato)


def toListCategory():
    dato = conn.readJSON()
    print("NOMBRE \t\t DESCRIPCION")
    for i in dato["Categorias"]:
        for value in i.values():
            print(value, end=" \t ")
        print("\n======================================================")


while True:
    print('[1] AGREGAR CATEGORIA')
    print('[2] ELIMINAR CATEGORIA')
    print('[3] LISTAR CATEGORIA')
    print('[4] SALIR DEL PROGRAMA')
    op = int(input('INGRESE LA OPCION: '))
    if op == 1:
        addCategory()
    elif op == 2:
        removeCategory()
    elif op == 3:
        toListCategory()
    elif op == 4:
        exit()
