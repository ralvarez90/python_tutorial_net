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


def showExample01():
    # objeto inmutable
    someInteger = 123
    print(f'some_int: {someInteger}, with id: {hex(id(someInteger))}')
    someInteger = 124
    print(f'some_int: {someInteger}, with id: {hex(id(someInteger))}')

    # objeto mutable
    someList = [1, 2, 3]
    print(f'some_list: {someList}, with id: {hex(id(someList))}')
    someList.append(4)
    print(f'some_list: {someList}, with id: {hex(id(someList))}')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue. . . ')
