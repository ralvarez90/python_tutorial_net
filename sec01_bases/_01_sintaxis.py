"""SINTAXIS

1. Identación
Python no maneja ; para establecer fin de sentencia. Emplea
identaciones.

2. Comentarios
Se emplea # para establecer comentarios de una línea y triples
comillas para comentarios de bloque.

3. Identificadores
Son nombres que se asignan a las variables, funciones, módulos,
clases y otros objetos.
"""
import keyword


def list_keywords():
    for kw in keyword.kwlist:
        print(kw)


def show_example():
    # mensaje de bienvenida
    print('Hello World in Python3')

    # se muestran palabras reservadas
    list_keywords()


def main():
    show_example()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . . ')
