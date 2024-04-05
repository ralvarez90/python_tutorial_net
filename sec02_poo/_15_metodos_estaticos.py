"""MÉTODOS ESTÁTICOS

A diferencia de los métodos de instancia, los métodos estáticos no 
están vinculados a un objeto. En otras palabras, los métodos estáticos 
no pueden acceder ni modificar el estado de un objeto.

Empleamos el decorador @staticmethod para establecer un método estático,
que es una variable de clase y no requiere recibir la referencia de la
clase en cuestión como primer argumento. Por lo tanto, los métodos estáticos 
no pueden acceder ni modificar el estado de la clase.

Invocamos un método estático de la forma:
className.static_method_name()

Los método estáticos y lo de clase son similares pero tienen sutiles
diferencias. La principal diferencia es que los classmethds pueden modificar
el estado de la clase mientras que los estáticos no.
"""


class TemperatureConverter:
    KELVIN = 'K'
    FAHRENHEIT = 'F'
    CELSIUS = 'C'

    @staticmethod
    def celsiusToFahrenheit(cAmount: float) -> float:
        return 9*cAmount/5 + 32

    @staticmethod
    def fahrenheitToCelsius(fAmount: float) -> float:
        return 5*(fAmount-32)/9

    @staticmethod
    def celsiusToKelvin(cAmount: float) -> float:
        return cAmount + 273.15

    @staticmethod
    def kelvinToCelsius(kAmount: float) -> float:
        return kAmount - 273.15

    @staticmethod
    def fahrenheitToKelvin(fAmount: float) -> float:
        return 5*(fAmount+459.67)/9

    @staticmethod
    def kelvinToFahrenheit(kAmount: float) -> float:
        return 9*kAmount/5 - 459.67

    @staticmethod
    def format(value: float, unit: str) -> str:
        match unit:
            case TemperatureConverter.FAHRENHEIT:
                symbol = '°F'
            case TemperatureConverter.CELSIUS:
                symbol = '°C'
            case TemperatureConverter.KELVIN:
                symbol = '°K'
            case _:
                symbol = ''
        return f'{value} {symbol}'


def showExample01():
    f = TemperatureConverter.celsiusToFahrenheit(35)
    print(TemperatureConverter.format(f, TemperatureConverter.FAHRENHEIT))


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
