"""REFERENCIAS

En python una variable no es una etiqueta de un valor. Las variables
almacenan referencias a objetos.

En otras palabras las variables son referencias a objetos en memoria.

1. Función id
Permite obtener la dirección de memoria del objeto referenciado en
una variable.

Pueden existir variables que apunten a una misma referencia 
en memoria. Una vez que un objeto en memoria no es referenciado
por ninguna variable el garbage collector se encarga de eliminar
dicha referencia.

Para obtener el número de referencias de un objeto empleamos el
módulo ctypes.
"""
from ctypes import c_long


def refCounter(address: int) -> int:
    return c_long.from_address(address).value


def showExample01():
    # referencia a entero
    counter1: int = 100
    counter2: int = counter1
    print(f'counter1: {counter1}, in memory address {hex(id(counter1))}')
    print(f'counter2: {counter2}, in memory address {hex(id(counter2))}')

    # conteo de referencias
    numbers = [1, 2, 3]
    idsNumbers = id(numbers)
    print(
        f'El arreglo numbers está referenciado en memoria {refCounter(idsNumbers)} veces')

    rank = numbers
    print(
        f'El arreglo numbers está referenciado en memoria {refCounter(idsNumbers)} veces')

    rank = None
    print(
        f'El arreglo numbers está referenciado en memoria {refCounter(idsNumbers)} veces')

    numbers = None
    print(
        f'El arreglo numbers está referenciado en memoria {refCounter(idsNumbers)} veces')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
