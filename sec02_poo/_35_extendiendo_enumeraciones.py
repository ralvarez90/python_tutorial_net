"""EXTENDIENDO ENUMERACIONES

Las enumeraciones son clases por lo que podemos agregar métodos o
implementarn dunder methods para customizar su comportamiento.

Si sobrescribirmos __str__ podemos personalizar como se mostrarán
cada uno de los campos dentro de una enumeración.

Si sobrescribimos el método __eq__ podemos establecer el comportamiento
que tendrán los miembros del enum al emplear el operador  ==.

Si sobrescirbimos __lt__ podemo establecer el criterio para considerar
los miembros de forma ordenada. Se emplea el decorador @total_ordering
del módulo functools.

Por default, todos los miembros dentro de una enumeración se evalúan 
como true si se pasan como argumento al constructor bool. Este
comportamiento se puede sobrescribir implementando __bool__.
"""
from enum import Enum
from functools import total_ordering
from typing import Literal


@total_ordering
class PaymentStatus(Enum):
    PENDING = 1
    COMPLETED = 2
    REFUNDED = 3

    def __str__(self) -> str:
        return f'{self.name.lower()}({self.value})'

    def __eq__(self, other: object) -> bool:
        if isinstance(other, int):
            return self.value == other

        if isinstance(other, PaymentStatus):
            return self is other

        return False

    def __lt__(self, other: object) -> bool:
        if isinstance(other, int):
            return self.value < other

        if isinstance(other, PaymentStatus):
            return self.value < other.value

        return False

    def __bool__(self) -> bool:
        if self is self.COMPLETED:
            return True
        return False


def show_example_01():
    print('Example 1. Show custom PaymentStatus members:')
    for ps in PaymentStatus:
        print(ps, end=', ')
    print()


def show_example_02():
    print('Example 2. Use __eq__ overloading operator:')
    print(PaymentStatus.PENDING == 1)


def show_example_03():
    status = 1
    if status < PaymentStatus.COMPLETED:
        print('The payment has not completed')
    status = PaymentStatus.PENDING
    if status >= PaymentStatus.COMPLETED:
        print('The payment is not pending')


def show_example_04():
    for member in PaymentStatus:
        print(member, bool(member))


def main():
    # run examples
    show_example_01()
    show_example_02()
    show_example_03()
    show_example_04()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
