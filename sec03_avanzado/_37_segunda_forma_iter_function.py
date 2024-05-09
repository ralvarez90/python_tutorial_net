"""SEGUNDA FORMA DE FUNCIÓN iter

Existe una segunda forma de implementación de la función iter, con
la firma:
iter(callable, sentinel)

Esta forma de la función iter recibe un callable y  un sentinela,
donde e valor sentinela se emplea para indicar si el iterador
continua o no
"""


def showExample01():

    # retorna un closure
    def counter():
        count = 0

        def increase():
            nonlocal count
            count += 1
            return count

        return increase

    cnt = counter()
    while True:
        current = cnt()
        print(current)
        if current == 3:
            break


def showExample02():

    class CounterIterator:
        def __init__(self, fn, sentinel) -> None:
            self.fn = fn
            self.sentinel = sentinel

        def __iter__(self):
            return self

        def __next__(self):
            current = self.fn()
            if current == self.sentinel:
                raise StopIteration
            return current

    def counter():
        count = 0

        def increase():
            nonlocal count
            count += 1
            return count
        return increase

    cnt = counter()
    iterator = CounterIterator(fn=cnt, sentinel=4)
    for count in iterator:
        print(count)


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
