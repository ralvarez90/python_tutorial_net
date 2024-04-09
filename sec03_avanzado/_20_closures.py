"""CLOSURES

En python podemos definir funciones dentro de otras. Estas se denominan
funciones anidadas.

Un closure una función anidada, que accede el estado que a una o más referencias
del la función que la contiente.

En python un "cell" generalmente se refiere a un "cell object" o "closure". Estos
se utilizan en el contexto de funciones anidas o closures. Un "cell" es escencialmente
un contenedor para una variables que es accesible tanto desde una función interna
desde la funciín  externa, aunque se defina en la función externa.

Para encontrar la dirección de memproa de un cell, puede usar la propiedad __closure__.

En Python, el atributo __closure__ es un atributo especial de las funciones que se 
refiere a una tupla de objetos "cell" que representan las variables libres 
(variables que están definidas en el ámbito de una función externa y se 
utilizan en una función interna) de la función.

Cuando una función tiene variables libres, Python utiliza "closures" para recordar 
los valores de estas variables incluso después de que la función externa haya 
finalizado su ejecución. El atributo __closure__ nos proporciona acceso a estos 
"cells" que contienen estos valores.
"""


def showExample01():

    def say():
        # greeting tiene es compartida por 2 scopes
        greeting: str = 'Hello'

        def display():
            print(greeting)

        return display

    saludar = say()
    saludar()


def showExample02():
    def outerFunction(x):
        def innerFunction(y):
            return x+y
        return innerFunction

    closure = outerFunction(10)
    result = closure(5)
    print(closure.__closure__)


def showExample03():
    def outerFunction(x: int):
        def innerFunction(y: int):
            return x+y
        return innerFunction

    closure = outerFunction(10)
    cells = closure.__closure__
    print(f'cells: {cells}')
    xValue = cells[0].cell_contents
    print(xValue)


def showExample04():

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
    showExample03()
    showExample04()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
