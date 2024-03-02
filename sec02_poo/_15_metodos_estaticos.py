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
    def celsius_to_fahrenheit(c_amount: float) -> float:
        return 9*c_amount/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f_amount: float) -> float:
        return 5*(f_amount-32)/9

    @staticmethod
    def celsius_to_kelvin(c_amount: float) -> float:
        return c_amount + 273.15

    @staticmethod
    def kelvin_to_celsius(k_amount: float) -> float:
        return k_amount - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(f_amount: float) -> float:
        return 5*(f_amount+459.67)/9

    @staticmethod
    def kelvin_to_fahrenheit(k_amount: float) -> float:
        return 9*k_amount/5 - 459.67

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


def show_example_1():
    f = TemperatureConverter.celsius_to_fahrenheit(35)
    print(TemperatureConverter.format(f, TemperatureConverter.FAHRENHEIT))


def main():
    show_example_1()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . .')
