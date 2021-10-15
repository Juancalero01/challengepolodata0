from Clases.autor import Autor
from Clases.categoria import Categoria
a = Autor()
c = Categoria()


# PRIMERA PARTE DEL PROYECTO


def registrarCategoria():
    c.nombre = input('INGRESE EL NOMBRE DE LA NUEVA CATEGORIA: ').capitalize()
    c.registrarCategoria(c.nombre)


def eliminarCategoria():
    c.listarCategoria()
    c.nombre = input('INGRESE EL NOMBRE DE LA CATEGORIA: ')
    c.eliminarCategoria(c.nombre)


def listarCategorias():
    c.listarCategoria()


# SEGUNDA PARTE DEL PROYECTO


def registrarAutor():
    a.nombre = input('INGRESE EL NOMBRE DEL NUEVO AUTOR: ').capitalize()
    a.apellido = input('INGRESE EL APELLIDO DEL NUEVO AUTOR: ').capitalize()
    a.registrarAutor(a.nombre, a.apellido)


def eliminarAutor():
    a.listarAutor()
    a.nombre = input('INGRESE EL NOMBRE DEl AUTOR QUE ELIMINARA: ')
    a.eliminarAutor(a.nombre)


def listarAutores():
    a.listarAutor()


# TERCERA PARTE DEL PROYECTO












while True:
    print('===========================')
    print('[1]REGISTRAR CATEGORIA')
    print('[2]ELIMINAR CATEGORIA')
    print('[3]LISTAR CATEGORIAS')
    print('===========================')
    print('[4]REGISTRAR AUTOR')
    print('[5]ELIMINAR AUTOR')
    print('[6]LISTAR AUTORES')
    print('===========================')
    print('[7]REGISTRAR LIBRO')
    print('[8]ELIMINAR LIBRO')
    print('[9]LISTAR LIBROS')
    print('===========================')
    op = input('INGRESE LA OPCION: ')
    if op == '1':
        registrarCategoria()
    elif op == '2':
        eliminarCategoria()
    elif op == '3':
        listarCategorias()
    elif op == '4':
        registrarAutor()
    elif op == '5':
        eliminarAutor()
    elif op == '6':
        listarAutores()
    elif op == '7':
        # listarAutores()
        pass
    elif op == '8':
        # eliminarAutor()
        pass
    elif op == '9':
        # listarAutores()
        pass
