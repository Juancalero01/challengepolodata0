from conexion import BaseDatos
from Clases.contadorLibro import Contador
from Clases.autor import Autor
import os
import time
os.system('cls')

a = Autor()
bd = BaseDatos
cont = Contador()


def añadirAutor():
    a.id = cont.contar()
    a.nombre = input('INGRESE EL NOMBRE DEL NUEVO AUTOR: ').capitalize()
    a.apellido = input('INGRESE EL APELLIDO DEL NUEVO AUTOR: ').capitalize()
    dato = bd.leerBd()
    dato["autores"].append(
        {
            "id": a.id,
            "nombre": a.nombre,
            "apellido": a.apellido
        }
    )
    bd.escribirBd(dato)
    print('SE REGISTRO CORRECTAMENTE')
    time.sleep(1)
    os.system('cls')


def eliminarAutor():
    dato = bd.leerBd()
    idAutor = int(input('INGRESE EL ID DEL AUTOR: '))
    for i in dato['autores']:
        for v in i.values():
            if v == idAutor:
                dato["autores"].remove(i)
    bd.escribirBd(dato)
    print('SE ELIMINO CORRECTAMENTE')
    time.sleep(1)
    os.system('cls')


def listarAutor():
    dato = bd.leerBd()
    print('ID \t NOMBRE \t APELLIDO')
    for i in dato['autores']:
        for v in i.values():
            print(v, end=" \t ")
        print("\n=================================")


while True:
    print('SEGUNDA PARTE DEL PROYECTO')
    print('[1]REGISTRAR AUTOR')
    print('[2]ELIMINAR AUTOR')
    print('[3]LISTAR AUTORES')
    print('[4]SALIR DEL PROGRAMA')
    op = input('INGRESE LA OPCION: ')
    if op == '1':
        os.system('cls')
        añadirAutor()
    elif op == '2':
        os.system('cls')
        listarAutor()
        eliminarAutor()
    elif op == '3':
        os.system('cls')
        listarAutor()
    elif op == '4':
        exit()
