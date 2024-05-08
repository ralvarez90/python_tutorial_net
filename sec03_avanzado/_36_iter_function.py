"""FUNCIÓN iter

Retorna el correspondiente iterador del objeto que
recibe como argumento.

Esta clase en realidad, requiere que su argumento sea
un objeto iterable o una secuencia.

Primero buscará el método __iter__ del objeto argumento
y si no existe buscará el __getitem__.

En el ejemplo 02, debido a que Counter implementa el 
método __getitem__() que devuelve un elemento basado en un 
índice, es una secuencia.

Ahora, puedes usar la función iter() para obtener el 
iterador del contador, ver ejemplo 02.

En el ejemplo 03, se agrega la clase CounterIterator a la clase
Counter implementando el protocolo Iterable.
"""


def showExample01():
    print('EXAMPLE 01. Using iter method with a none sequence or iterable')

    class Counter:
        def __init__(self) -> None:
            self.__current = 0

    # lanza excepción
    counter = Counter()
    # iterator = iter(counter)


def showExample02():
    print('EXAMPLE 02. Using iter method and adding __getiten__ method in class.  Instances of'
          '\nthis classes are sequence now')

    class Counter:
        def __init__(self) -> None:
            self.current = 0

        def __getitem__(self, index: int):
            if isinstance(index, int):
                self.current += 1
                return self.current

    # get instance
    counter = Counter()
    iterator = iter(counter)
    print(f'Type(iterator) -> {type(iterator)}')


def showExample03():

    class Counter:
        def __init__(self) -> None:
            self.current = 0

        def __getitem__(self, index: int):
            if isinstance(index, int):
                self.current += 1
                return self.current

        def __iter__(self):
            return CounterIterator(counter=self)

    class CounterIterator:
        def __init__(self, counter: Counter) -> None:
            self.__counter = counter

        def __iter__(self):
            return self

        def __next__(self):
            self.__counter.current += 1
            return self.__counter.current

    # run ejemplo
    counter = Counter()
    iterator = iter(counter)
    print(type(iterator))


def main():
    showExample01()
    showExample02()
    showExample03()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
