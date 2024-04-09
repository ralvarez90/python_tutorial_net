"""DECORADORES CON ARGUMENTOS

Recordemos que los decoradores son funciones que 
reciben como argumento otra función, la modifican
y la vuelven a retornar.

Al ser funciones pueden o no recibir argumentos. La definición
forma de un decorador es:
- Funcion que toma otra como argumento y retorna otra función o
closure.
"""


def showExample01():
    """Version sin uso de decorador."""

    def getNetPrice(price: float, tax: float) -> float:
        return price * (1+tax)

    def currency(fn):
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            return f'{result}'
        return wrapper

    # decoramos funcion getNetPrice
    getNetPrice = currency(getNetPrice)
    print(getNetPrice(100, 0.05))


def showExample02():
    """Version con uso de decorador."""

    def currency(fn):
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            return f'{result}'
        return wrapper

    @currency
    def getNetPrice(price: float, tax: float) -> float:
        return price * (1+tax)
    print(getNetPrice(100, 0.05))


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
