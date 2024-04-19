"""FUNCIONES

Son bloques de código reutilizables que regresan un valor. Si no se 
especifica el valor a retornar con una sentencia return, se retorna 
un None de forma implícita.

Python incluye funciones built-in listas para usar.
"""


def greeting():
    print('Nos salvaste, estamos agradecidos')


def sayHi():
    print('Hi!')


def showExample01():
    sayHi()
    greeting()


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
