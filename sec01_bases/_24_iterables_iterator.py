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


def iter_example_v1():
    colors = ['red', 'green', 'blue']
    colors_iter = iter(colors)
    for _ in range(len(colors)):
        print(next(colors_iter))


def iter_example_v2():
    colors = ['red', 'green', 'blue']
    colors_iter = iter(colors)
    for item in colors_iter:
        print(item)


def main():
    # iterator1
    iter_example_v1()

    # iterador2
    iter_example_v2()


if __name__ == '__main__':

    # run application
    main()

    # end message
    input('\nPress any key to continue . . . ')
