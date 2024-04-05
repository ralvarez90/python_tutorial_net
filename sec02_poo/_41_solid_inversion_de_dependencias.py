"""PRINCIPIO DE INVERSIÓN DE DEPENDENCIAS

Este principio establece que
- Los módulos de alto nivel no deberían depender de módulos de bajo 
nivel. Ambos deberían depender de abstracciones.
- Las abstracciones no deberían depender de los detalles. 
Los detalles deberían depender de abstracciones.

El principio de inversión de dependencia tiene como objetivo reducir 
el acoplamiento entre clases creando una capa de abstracción entre ellas.
"""
from abc import ABC, abstractmethod


class CurrencyConverter(ABC):
    @abstractmethod
    def convert(self, fromCurrency: str, toCurrency: str, amount: float) -> float:
        pass


class AlphaConverter(CurrencyConverter):
    def convert(self, fromCurrency: str, toCurrency: str, amount: float) -> float:
        print('Converting currencya via Alpha API')
        print(f'{amount} {fromCurrency} = {amount*1.2} {toCurrency}')
        return amount*1.5


class FXConverter(CurrencyConverter):
    def convert(self, fromCurrency: str, toCurrency: str, amount: float) -> float:
        print('Converting currency via FX API')
        print(f'{amount} {fromCurrency} = {amount*1.2} {toCurrency}')
        return amount*2


class App:
    def __init__(self, converter: CurrencyConverter) -> None:
        self.converter = converter

    def start(self):
        self.converter.convert('EUR', 'USD', 100)


def showExample01():
    converter: CurrencyConverter = FXConverter()
    app = App(converter)
    app.start()


def showExample02():
    converter: CurrencyConverter = AlphaConverter()
    app = App(converter)
    app.start()


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
