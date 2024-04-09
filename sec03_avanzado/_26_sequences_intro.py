"""SECUENCIAS

Una secuencia es una colección de datos y posicionalmente ordenados. En
python una sequencia se indexa por índices que van del 0 a su longitud
-1.

Python cuenta con las siguientes secuencias construidas en el lenguaje
- list
- bytearrays
- strings
- tuplas
- ranges
- bytes

Python clasifica las secuencias como mutables e inmutables. Las secuencias
inmutables son los strings, tuplas, rangos y bytes mientras que las 
secuencias mutables son las listas, y los bytearrays.
"""
from typing import Sequence


def showExample01():
    message: str = 'Hello World!'
    print(isinstance(message, Sequence))


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to contine . . .')
