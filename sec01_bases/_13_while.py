"""WHILE

Permite ejecutar un bloque de código mientras la condición
a evaluar sea True. Pude anidárcele un bloque else que se ejecuta
cuando la condición se deja de cumplir.

Podemos además definir un nombre de variable empleando el símbolo
de asignación :=, que crea una variable dentro del scope del
while. Ver ejemplo 02.
"""
import random


def showExample01():
    command = ''
    while command.lower() != 'quit':
        command = input('>>> ')
        print(f'Echo: {command}')
    print()


def showExample02():
    intentos = 0
    while (numero := random.randint(1, 100)) != 10:
        intentos += 1
        print(f'intento {intentos}, Sin adivinar, fue {numero}')
    else:
        print(f'Intento {intentos}, encontrado: {numero}')


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
