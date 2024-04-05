"""SCOPE GLOBAL

Básicamente es el alcance que se tiene dentro de un
módulo. La palabra reservada global permite referencia
variables globales dentro de funciones, ya que cada 
función tiene su pripio scope local.

El scope global está contenido dentro de otro scope
conicido como built-in. 
"""

# variable global
counter: int = 10


def showExample01():
    print(f'Global variable: {counter}')


def showExample02():
    global counter
    print('Actualizando contador global...')
    counter += 1


def showExample03():
    print(f'Global variable: {counter}')


def main():
    showExample01()
    showExample02()
    showExample03()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
