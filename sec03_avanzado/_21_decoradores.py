"""DECORADORES

Un decorador es una función que toma otra como argumento y extiende su funcionalidad
retornando la función argumento con su funcionalidad extendida.

Recordemos que por definición un decorador es una función que recibe
otra función como argumento.
"""


def showExample01():

    def netPrice(price: float, tax: float):
        return price * (1 + tax)

    def currency(fn):
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            return f'${result}'
        return wrapper

    netPrice = currency(fn=netPrice)
    print(netPrice(100, 0.05))


def showExample02():
    pass


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
