"""ENUM auto

Dentro del módulo enum existe una helper clase llamada auto() que nos
permite ir generarndo enteros de forma consegutiva sin necesidad de
establecerlo de forma explícita.

De manera técnica, auto invoca al método _generate_next_value() para
generar valores para los miembros de la enumeración. Es posible 
sobrescribir para modificar su comportamiento default.
"""
from enum import Enum, auto


class State(Enum):
    PENDING = auto()
    FULFILLED = auto()
    REJECTED = auto()

    def __str__(self) -> str:
        return f'{self.name}({self.value})'


def showExample01():
    for state in State:
        print(state.name, state.value, state)


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
