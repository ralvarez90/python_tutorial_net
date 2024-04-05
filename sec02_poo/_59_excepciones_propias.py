"""CUSTOM EXCEPTIONS

Para crear excepciones propias puede definir su clase propia 
extendiendo a Exception.

Como a cualquier otra clase, podemos añadirles funcionalides
como propiedades y métodos.

En la práctica, querrás mantener organizadas las excepciones 
personalizadas creando una jerarquía de excepciones personalizada. 

La jerarquía de excepciones personalizada le permite detectar 
excepciones en múltiples niveles, como las clases de excepción 
estándar.
"""


class FahrenheitError(Exception):
    minF = 32
    maxF = 212

    def __init__(self, f: float,  *args: object) -> None:
        super().__init__(args)
        self.f = f

    def __str__(self) -> str:
        return f'The {self.f} is not in a valida range {self.minF, self.maxF}'


def fahrenheitToCelsius(f: float) -> float:
    if f < FahrenheitError.minF or f > FahrenheitError.maxF:
        raise FahrenheitError(f)
    return (f-32) * 5/9


def showExample01():
    f = input('Enter a temperature in Fahrenheit:')
    try:
        f = float(f)
    except ValueError as ex:
        print(ex)
    else:
        try:
            c = fahrenheitToCelsius(float(f))
        except FahrenheitError as ex:
            print(ex)
        else:
            print(f'{f} Fahrenheit = {c:.4f} Celsius')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
