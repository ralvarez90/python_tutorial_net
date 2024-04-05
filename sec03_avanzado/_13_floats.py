"""FLOAT

La implementación CPython usa el tipo de dato double para implementar
el tipo de dato float en python.

Python usa 64 bits para representar estos números y su tamaño es fijo,
cosa que no pasa con el tipo de datos int.

De manera técnica python usa 64 bits de la siguiente forma:
- 1 bit para el signo
- 11 bits para el exponente [-1022, 2023]
- 53 bits para dígitos cignificativos.

Cualquier objeto se puede pasar como argumento a a clase float, y
este invocará al dunder método __float__

Al usar print se puede emplear el método format para
establecer formato específico a números flotantes.

# todo, agregar nota y leccion sobre isclose del módulo math
"""


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __float__(self):
        print(f'Se invocó el método __float__')
        return float(self.age)


def showExample01():
    print(float(1.23))
    print(float('1.23'))


def showExample02():
    p = Person('John Wick', 45)
    print(float(p))


def showExample03():
    print(format(123.123, '.20f'))


def main():
    showExample01()
    showExample02()
    showExample03()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
