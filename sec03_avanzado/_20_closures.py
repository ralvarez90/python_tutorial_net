"""CLOSURES

En python podemos definir funciones dentro de otras. Estas se denominan
funciones anidadas.

Un closure es una función anidada, que accede el estado que a una o más referencias
del la función que la contiente.
"""


def showExample01():

    def say():
        # greeting tiene es compartida por 2 scopes
        greeting: str = 'Hello'

        def display():
            # es un closure
            print(greeting)

        return display

    saludar = say()
    saludar()


def showExample02():

    def say():
        greeting = 'Hello'
        print(hex(id(greeting)))

        def display():
            print(hex(id(greeting)))
            print(greeting)

        return display

    fn = say()
    fn()


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
