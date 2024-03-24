"""OVERRIDING METHOD

La sobrescritura de métodos consiste en volver a reimplementar el
cuerpo de un método en las clases hijas con la finalidad de adaptar
el comportamiento de dicho método. Se puede reutilizar o no el cuerpo
del método en el padre.

La sobreescritura permite implemnentar el polimorfismo a través de
la gerarquía de herencia.

Al invocar un método de instancia, primer busca dentro de su diccionario
__dict__.

La sobrescritura se puede extender a variables de clase y de instancia.
"""
import re


class Employee:

    def __init__(self, name: str, basepay: float) -> None:
        self.name = name
        self.basepay = basepay

    def getPay(self) -> float:
        return self.basepay

    def __str__(self) -> str:
        return f'Employee{self.__dict__}'


class SalesEmployee(Employee):

    def __init__(self, name: str, basepay: float, incentive: float) -> None:
        super().__init__(name, basepay)
        self.incentive = incentive

    def getPay(self) -> float:
        return super().getPay() + self.incentive

    def __str__(self) -> str:
        return f'SalesEmployee{self.__dict__}'


class Parser:
    phonePattenr = r'\d{3}-\d{3}-\d{4}'

    def __init__(self, text: str) -> None:
        self.text = text

    def email(self) -> str:
        match = re.search(
            r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', self.text)
        if match:
            return match.group(0)
        return None

    def phone(self):
        match = re.search(self.phonePattenr, self.text)
        if match:
            return match.group(0)
        return None

    def parse(self):
        return {
            'email': self.email(),
            'phone': self.phone(),
        }


class UKParser(Parser):
    phonePattern = r'(\+\d{1}-\d{3}-\d{3}-\d{4})'


def showExample01():
    emp1: Employee = Employee('John Wick1', 1_000_000)
    emp2: Employee = SalesEmployee('John Wick2', 1_000_000, 100_000)
    print(f'emp1 has a pay: ${emp1.getPay():,.2f}')
    print(f'emp2 has a pay: ${emp2.getPay():,.2f}')


def showExample02():
    s = 'Contact us via 408-205-5663 or email@test.com'
    parser: Parser = Parser(text=s)
    print(parser.parse())


def showExample03():
    s = 'Contact me via +1-650-453-3456 or email@test.co.uk'
    parser: Parser = UKParser(text=s)
    print(parser.parse())


def main():
    showExample01()
    showExample02()
    showExample03()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
