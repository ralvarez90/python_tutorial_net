"""MÉTODO MRO (Method Resolution Order)

Cuando clase padres de una clase hija tienen métodos con el mismo nombre y 
la clase secundaria llama al método, Python usa el método mro para buscar 
el método correcto para llamar.
"""


class Flyable:

    def start(self):
        print('Start the Flyable object')

    def fly(self):
        pass


class Car:

    def start(self):
        print('Start the Car object')

    def go(self):
        pass


class FlyingCar(Flyable, Car):

    def start(self):
        return super().start()


def showExample01():
    car = FlyingCar()
    car.start()
    print(f'FlyingCar.__mro__: {FlyingCar.__mro__}')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
