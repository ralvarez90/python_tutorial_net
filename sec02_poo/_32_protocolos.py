"""PROTOCOLS

Los protocolos en Python son una forma informal de especificar interfaces. 
En lugar de depender de una interfaz formal como en algunos lenguajes 
orientados a objetos, Python confía en la implementación correcta de 
métodos y atributos por parte de las clases que se adhieren a un 
protocolo.

En el duck typing, los comportamientos y propiedades de un objeto 
determinan el tipo de objeto, no el tipo explícito del objeto.

Por ejemplo, un objeto con cantidad y precio seguirá el protocolo Item, 
independientemente de su tipo explícito.

El duck typing está inspirada en la prueba del pato: Si camina como un pato 
y grazna como un pato, entonces debe ser un pato.

En la práctica, cuando escribes una función que acepta entradas, te preocupas 
más por el comportamiento y las propiedades de la entrada, no por su 
tipo explícito.

En resumen, se emplean para definir interfaces implícitas.
"""
from typing import List, Protocol


class Item(Protocol):
    """Cualquier objeto que tenga las propiedades y métodos de este protocolo,
    es decir, que cumplan con este protocolo cumplirán la relación 'es un' Item.
    """
    quantity: int
    price: float


class Product:

    def __init__(self, name: str, quantity: int, price: float) -> None:
        self.name = name
        self.quantity = quantity
        self.price = price


class Stock:

    def __init__(self, productname: str, quantity: int, price: float) -> None:
        self.productname = productname
        self.quantity = quantity
        self.price = price


def gettotal(items: list[Item]) -> float:
    return sum([item.quantity*item.price for item in items])


def show_example_01():
    total = gettotal([
        Product('Product1', 10, 100),
        Product('Product2', 20, 100),
        Product('Product3', 30, 100),
        Product('Product4', 40, 100),
        Product('Product5', 50, 100),
    ])

    print(f'Total: ${total:,.2f}')


def show_example_02():
    total = gettotal([
        Stock('Tablet', 5, 950),
        Stock('Laptop', 10, 850),
    ])

    print(f'Total: ${total:,.2f}')


def main():
    show_example_01()
    show_example_02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
