"""MÉTODOS

Son funciones asociadas a instancias de clases o clases.
Un método puede ser de instancia, de clase o estático.

Métodos de instancia
Son métodos que se invocan desde los objetos. Reciben como
primer argumento al definirse un parámetro self que hace
referencia a la misma instancia en cuestión.

Métodos de clase y estáticos
Se invocan desde las clases que los contienen. No es necesario
general instancias.
"""


class Person:
    counter: int = 0

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.counter += 1

    def agradecer(self):
        print(f'Hi, it is {self.name}')

    @classmethod
    def obtenerAnonimo(cls):
        return Person(name='Anonymous', age=22)

    def __str__(self) -> str:
        return f'Person{self.__dict__}'


class TemperatureConverter:
    @staticmethod
    def celsiusToFahrenheit(c: float) -> float:
        return 9 * c/5 + 32

    @staticmethod
    def fahrenheitToCelsius(f: float) -> float:
        return 5 * (f-32)/9


def showExample01():
    # ejemplo 1
    p1 = Person(name='John Wick', age=33)
    p2 = Person.obtenerAnonimo()
    print(p1) or print(p2)
    print('-'*50)


def showExample02():
    r1 = TemperatureConverter.celsiusToFahrenheit(1)
    r2 = TemperatureConverter.fahrenheitToCelsius(1)
    print(r1)
    print(r2)


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
