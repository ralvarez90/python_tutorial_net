"""ANOTACIONES DE TIPO

Las sugerencias de tipo de python le brindan escritura estática 
opcional para aprovechar lo mejor de la escritura estática y 
dinámica.

Python en el módulo typing incluye alias de tipos que son
List, Tuple, Dict, Set, Frozenset, Sequence, Mapping, 
ByteString, etc.
"""


def sayHi(name: str):
    print(f'Hello {name}')


def runtimeType(obj: object) -> str:
    return str(type(obj))[8:-2]


if __name__ == '__main__':

    # ejemplos
    print(runtimeType(None))
    sayHi(name=input('nombre: '))

    # end application
    input('\nPress any key to continue . . .')
