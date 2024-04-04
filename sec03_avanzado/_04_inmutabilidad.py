"""MUTABILIDAD

En python cualquier cosa es un objeto. Cada objeto tiene un
estado interno. Algunos objetos permiten cambiar su estado
interno mientras que otros no, estos últimos se denominan
inmutables.

Algunos ejemplos de objetos inmutables son:
strings
números
booleanos
tuplas
frozensets

Algunos ejemplos de objetos mutables son
listas
conjuntos
diccionarios

Clases definidas por el usuario (user defined classes) pueden ser
mutables o inmutables, esto quiere decir que sus objetos podrán
ser mutables o inmutables.
"""


def show_example_01():
    # objeto inmutable
    some_int = 123
    print(f'some_int: {some_int}, with id: {hex(id(some_int))}')
    some_int = 124
    print(f'some_int: {some_int}, with id: {hex(id(some_int))}')

    # objeto mutable
    some_list = [1, 2, 3]
    print(f'some_list: {some_list}, with id: {hex(id(some_list))}')
    some_list.append(4)
    print(f'some_list: {some_list}, with id: {hex(id(some_list))}')


def main():
    show_example_01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue. . . ')
