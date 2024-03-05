"""HERENCIA MÚLTIPLE

Cuando una clase hereda únicamente de otra clase se denomina 
herancia múltiple. Python permite heredar de múltiples clases.

Si una clase hereda de dos o más clases se denomina herencia
múltiple.

Para extender una clase de múltiples clases se hace de la forma:
class NombreClase(ParentClass1, ParentClass2, ..., ParentClassN)
"""


class Car:

    def go(self):
        print('Going...')


class Flyable:

    def fly(self):
        print('Flying...')


class FlyingCar(Flyable, Car):
    pass


def run_example_1():
    fc = FlyingCar()
    fc.go()
    fc.fly()


def main():
    run_example_1()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . .')
