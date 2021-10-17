from Clases.autor import Autor
from Clases.categoria import Categoria
from Clases.libro import Libro
import os
from time import sleep

# Github https://github.com/Juancalero01/testJson-py


def clear():
    return os.system('cls')


a = Autor()
c = Categoria()
l = Libro()


def registrarCategoria():
    c.nombre = input('INGRESE EL NOMBRE DE LA NUEVA CATEGORIA: ').capitalize()
    c.registrarCategoria(c.nombre)
    sleep(1)
    print('SE REGISTRO CORRECTAMENTE ')
    sleep(2)
    clear()


def eliminarCategoria():
    c.listarCategoria()
    idCategoria = int(input('INGRESE EL ID DE LA CATEGORIA: '))
    c.eliminarCategoria(idCategoria)
    sleep(1)
    print('SE ELIMINO CORRECTAMENTE ')
    sleep(2)
    clear()


def registrarAutor():
    a.nombre = input('INGRESE EL NOMBRE DEL NUEVO AUTOR: ').capitalize()
    a.apellido = input('INGRESE EL APELLIDO DEL NUEVO AUTOR: ').capitalize()
    a.registrarAutor(a.nombre, a.apellido)
    sleep(1)
    print('SE REGISTRO CORRECTAMENTE ')
    sleep(2)
    clear()


def eliminarAutor():
    a.listarAutor()
    idAutor = int(input('INGRESE EL ID DEL AUTOR: '))
    a.eliminarAutor(idAutor)
    sleep(1)
    print('SE ELIMINO CORRECTAMENTE ')
    sleep(2)
    clear()


def registrarLibro():
    l.titulo = input('INGRESE EL TITULO DEL LIBRO: ')
    c.listarCategoria()
    idCategoria = int(input('INGRESE EL ID DE LA CATEGORIA: '))
    l.categoria = c.retornarCategoria(idCategoria)
    a.listarAutor()
    idAutor = int(input('INGRESE EL ID DEL AUTOR: '))
    nombre, apellido = a.retornarAutor(idAutor)
    l.autor = f"{nombre} {apellido}"
    l.registrarLibro(l.titulo, l.categoria, l.autor)
    sleep(1)
    print('SE REGISTRO CORRECTAMENTE ')
    sleep(2)
    clear()


def eliminarLibro():
    l.listarLibro()
    idLibro = int(input('INGRESE EL ID DEL LIBRO: '))
    l.eliminarLibro(idLibro)
    sleep(1)
    print('SE ELIMINO CORRECTAMENTE ')
    sleep(2)
    clear()


def categorias():
    while True:
        print('===========================')
        print('[1]REGISTRAR CATEGORIA')
        print('[2]ELIMINAR CATEGORIA')
        print('[3]LISTAR CATEGORIAS')
        print('[4]CERRAR')
        print('===========================')
        op = input('INGRESE LA OPCION: ')
        if op == '1':
            clear()
            registrarCategoria()
        elif op == '2':
            clear()
            eliminarCategoria()
        elif op == '3':
            clear()
            c.listarCategoria()
            input('PRESIONE ENTER PARA SALIR.. ')
            clear()
        elif op == '4':
            break


def autores():
    while True:
        print('===========================')
        print('[1]REGISTRAR AUTOR')
        print('[2]ELIMINAR AUTOR')
        print('[3]LISTAR AUTORES')
        print('[4]CERRAR')
        print('===========================')
        op = input('INGRESE LA OPCION: ')
        if op == '1':
            clear()
            registrarAutor()
        elif op == '2':
            clear()
            eliminarAutor()
        elif op == '3':
            clear()
            a.listarAutor()
            input('PRESIONE ENTER PARA SALIR.. ')
            clear()
        elif op == '4':
            break


def libros():
    while True:
        print('===========================')
        print('[1]REGISTRAR LIBRO')
        print('[2]ELIMINAR LIBRO')
        print('[3]LISTAR LIBROS')
        print('[4]CERRAR')
        print('===========================')
        op = input('INGRESE LA OPCION: ')
        if op == '1':
            clear()
            registrarLibro()
        elif op == '2':
            clear()
            eliminarLibro()
        elif op == '3':
            clear()
            l.listarLibro()
            input('PRESIONE ENTER PARA SALIR.. ')
            clear()
        elif op == '4':
            break


while True:
    clear()
    print('===========================')
    print('[1]CATEGORIAS')
    print('[2]AUTORES')
    print('[3]LIBROS')
    print('===========================')
    op = input('INGRESE LA OPCION: ')
    if op == '1':
        clear()
        categorias()
    elif op == '2':
        clear()
        autores()
    elif op == '3':
        clear()
        libros()
