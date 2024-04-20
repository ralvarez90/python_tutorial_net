"""SOBRECARGA DE OPERADORES

Permiten operar objetos de forma polimórfica. Estos sobrecargan
los operadores:
+       __add__
-       __sub__
*       __mul__
/       __truediv__
//      __floordiv__
%       __mod__
**      __pow__
>>      __rshift__
>>      __lshift__
&       __and__
|       __or__
^       __xor__

Existen otros métodos que permiten sobrecargar operadores como +=, -=,
*=, etc...
"""
import math


class Point2D:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def __add__(self, __value: object) -> 'Point2D':
        if not isinstance(__value, Point2D):
            raise ValueError('The other must be an instance of Point2D')
        return Point2D(x=self.x + __value.x, y=self.y + __value.y)

    def __sub__(self, __value: object) -> 'Point2D':
        if not isinstance(__value, Point2D):
            raise ValueError('The other must be an instance of Point2D')
        return Point2D(x=self.x - __value.x, y=self.y - __value.y)

    @property
    def length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'


class Item:
    def __init__(self, name: str, qty: int, price: float):
        self.name = name
        self.qty = qty
        self.price = price

    @property
    def amount(self) -> float:
        return self.qty * self.price

    def __str__(self) -> str:
        return f'{self.__dict__}'


class Cart:
    def __init__(self) -> None:
        self.items: list[Item] = []

    @property
    def total(self) -> float:
        return sum([item.amount for item in self.items])

    def __iadd__(self, item: Item):
        if not isinstance(item, Item):
            raise ValueError('The item must be an Item instance.')
        self.items.append(item)
        return self

    def __str__(self) -> str:
        if not self.items:
            return 'The cart is empty'
        return '\n'.join([str(item) for item in self.items])


def showExample01():
    i = Point2D(1, 0)
    j = Point2D(0, 1)
    unit: Point2D = i+j
    print(f'i     -> {i} with length:', i.length)
    print(f'j     -> {j} with length:', j.length)
    print(f'i + j -> {unit} with lenght: {unit.length:.2f}')


def showExample02():
    cart = Cart()
    cart += Item(name='Apple', qty=5, price=2)
    cart += Item(name='Banana', qty=20, price=1)
    cart += Item(name='Orange', qty=10, price=1.5)
    print(cart)
    print('-'*30)
    print(f'Total: ${cart.total:,.2f}')


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
