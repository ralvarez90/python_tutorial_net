"""WHILE

Permite ejecutar un bloque de código mientras la condición
a evaluar sea True. Pude anidárcele un bloque else que se ejecuta
cuando la condición se deja de cumplir.
"""
import random


def whileExampleV1():
    command = ''
    while command.lower() != 'quit':
        command = input('>>> ')
        print(f'Echo: {command}')
    print()


def whileExampleV2():
    intentos = 0
    while (numero := random.randint(1, 100)) != 10:
        intentos += 1
        print(f'intento {intentos}, Sin adivinar, fue {numero}')
    else:
        print(f'Intento {intentos}, encontrado: {numero}')


if __name__ == '__main__':

    # while
    whileExampleV1()

    # while v2
    whileExampleV2()

    # end application
    input('\nPress any key to continue . . . ')
