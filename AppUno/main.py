from conexion import BaseDatos
from Clases.contadorCategorias import Contador
from Clases.categoria import Categoria
import os
import time
os.system('cls')

c = Categoria()
bd = BaseDatos
cont = Contador()


def añadirCategoria():
    c.id = cont.contar()
    c.nombre = input('INGRESE EL NOMBRE DE LA NUEVA CATEGORIA: ').capitalize()
    dato = bd.leerBd()
    dato["categorias"].append(
        {
            "id": c.id,
            "nombre": c.nombre
        }
    )
    bd.escribirBd(dato)
    print('SE REGISTRO CORRECTAMENTE')
    time.sleep(1)
    os.system('cls')


def eliminarCategoria():
    dato = bd.leerBd()
    idCategoria = int(input('INGRESE EL ID DE LA CATEGORIA: '))
    for i in dato['categorias']:
        for v in i.values():
            if v == idCategoria:
                dato["categorias"].remove(i)

    bd.escribirBd(dato)
    print('SE ELIMINO CORRECTAMENTE')
    time.sleep(1)
    os.system('cls')


def listarCategoria():
    dato = bd.leerBd()
    print('ID \t NOMBRE')
    for i in dato['categorias']:
        for v in i.values():
            print(v, end=" \t ")
        print("\n================")


while True:
    print('PRIMERA PARTE DEL PROYECTO')
    print('[1]REGISTRAR CATEGORIA')
    print('[2]ELIMINAR CATEGORIA')
    print('[3]LISTAR CATEGORIAS')
    print('[4]SALIR DEL PROGRAMA')
    op = input('INGRESE LA OPCION: ')
    if op == '1':
        os.system('cls')
        añadirCategoria()
    elif op == '2':
        os.system('cls')
        listarCategoria()
        eliminarCategoria()
    elif op == '3':
        os.system('cls')
        listarCategoria()
    elif op == '4':
        exit()
