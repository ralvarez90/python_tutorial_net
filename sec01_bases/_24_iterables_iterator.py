"""ITERABLES

En python, un iterable es un objeto que incluye cero, 1 o más
elementos.

Un iterable tiene la habilidad de regresar sus elementos uno
a la vez. Debido a esta característica puede usar el ciclo for
con iterables.

Algunos iterables son los range, strings, listas y tuplas.

1. Iterator
En Python, "iter" es una función que se utiliza para obtener un iterador 
a partir de un objeto iterable. Un objeto iterable es aquel que
puede ser recorrido. 

Podemos iterar un iterador con el for o mediante la función next, que
permite obtener el siguiente elemento en la secuencia. Si se invoca
next y ya no hay más elementos que devolver en el iterador, se lanza
una excepción.

Un iterador es stateful, quiere decir que una vez que se consume
cada elemento de su interior este se elimina.
"""


def showExample01():
    colors = ['red', 'green', 'blue']
    colorsIterator = iter(colors)
    for _ in range(len(colors)):
        print(next(colorsIterator))


def showExample02():
    colors = ['red', 'green', 'blue']
    colorsIterator = iter(colors)
    for item in colorsIterator:
        print(item)


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
