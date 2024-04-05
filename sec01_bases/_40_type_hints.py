"""ANOTACIONES DE TIPO

Las sugerencias de tipo de python le brindan escritura estática 
opcional para aprovechar lo mejor de la escritura estática y 
dinámica.

Python en el módulo typing incluye alias de tipos que son
List, Tuple, Dict, Set, Frozenset, Sequence, Mapping, 
ByteString, etc.

Existen librerías externas que nos ayudan a realizar ciertos
chequeos de tipos como si python se tratase un lenguaje con
un sistema de tipos estáticos.

Una de las librerías antes mencionadas es mypy. Por otro
lado el módulo typing nos ayuda con alias de clases para
poder usar como anotaciones de tipos.

Se conciedera una Union[tipo1, tipo2] como un objeto que
puede ser instancia de tipo1, o de tipo2. A partir de
python 3.10 se puede usar el | como alternativa.

Los alias, son asignaciones de tipos de forma que nos
permite crear nombres de tipos personalizados.

Existen alias de colecciones como listas, tuplas, etc. Que
son List, Tuple, Dict, Set, Frozenset, Sequence, Mapping y
ByteString
"""
from typing import List


# generamos alias
Complex = complex
Double = float
Integer = int
Numeric = Complex | Double | Integer


def sayHi(name: str):
    print(f'Hello {name}')


def runtimeType(obj: object) -> str:
    return str(type(obj))[8:-2]


def obtenerSuma(x: Numeric, y:    Numeric) -> Numeric:
    return x+y


def obtenerProducto(x: Numeric, y: Numeric) -> Numeric:
    return x*y


def showExample01():
    print(runtimeType(None))
    sayHi(name=input('nombre: '))
    print(f'5+6 = {obtenerSuma(5, 6)}')
    print(f'5*6 = {obtenerProducto(5, 6)}')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
