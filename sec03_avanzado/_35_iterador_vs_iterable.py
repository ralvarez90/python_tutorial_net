"""ITERATOR VS ITERABLES

1. Iterator
Objeto que implementa en su clase el protocolo iterator. Es decir
tiene definidos __iter__ y __next__.

2. Iterables
Un iterable es un objeto que puede iterar, es decir, en su interior
tiene un iterador.

Un iterable es aquel objeto que tiene __iter__ implementado.

3. Método iter
Podemos obtener el iterador de un objeto iterable empleando
la clase iter.

4. Método next
Se emplea para obtener el siguiente elemento entregado por un
iterador.

Podemos separar el iterador de un iterable.  Ver ejemplo
"""


def runtimeType(obj: object) -> str:
    return str(type(obj))[8:-2]


def showExample01():
    print('EXAMPLE 01. Get iterator from a list.')
    numbers = [1, 2, 3]
    numbersIterator = numbers.__iter__()
    print(f'numbers.__iter__()  :  {numbersIterator}')
    print(f'type of (numbersIterator) : {runtimeType(numbersIterator)}')


def showExample02():
    print('EXAMPLE 02. Get iterator object using iter function.')
    numbers = [1, 2, 3]
    numbersIterator = iter(numbers)
    for _ in range(len(numbers)):
        print(next(numbersIterator))


def showExample03():
    print('EXAMPLE 03. Using class with iterable protocol')

    class Colors:
        def __init__(self) -> None:
            self.rgb = ['red', 'green', 'blue']
            self.__index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.__index >= len(self.rgb):
                raise StopIteration

            # return the next color
            color = self.rgb[self.__index]
            self.__index += 1
            return color

    # iterabmos colors
    colors = Colors()
    for c in colors:
        print(c)


def showExample04():

    # iterable
    class Colors:
        def __init__(self) -> None:
            self.rgb = ['red', 'green', 'blue']

    # iterador

    # test


def main():
    showExample01()
    showExample02()
    showExample03()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
