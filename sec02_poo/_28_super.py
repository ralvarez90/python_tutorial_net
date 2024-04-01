"""PALABRA RESERVADA SUPER

Esta palabra hace referencia a la clase padre inmediata dentro de
otra clase.  Esto nos permite hacer referencia a cualquier atributo
o método dentro de la clase padre.

La palabra reserva super permite evitar duplicados de código, 
permitiendo de forma directa la reutilización de elementos como 
propiedaes o métodos del padre.
"""


class Employee:
    def __init__(self, name: str, basepay: float, bonus: float) -> None:
        assert name != '', 'Name value cannot be an empty string'
        assert basepay >= 0 and bonus >= 0, 'Monetary values cannot be a negative amount'
        self.name = name
        self.basepay = basepay
        self.bonus = bonus

    def getpay(self) -> float:
        return self.basepay + self.bonus


class SalesEmployee(Employee):
    def __init__(self, name: str, basepay: float, bonus: float, sales_incentive: float) -> None:
        super().__init__(name, basepay, bonus)
        assert sales_incentive >= 0, 'Sales incentive cannot be a negative number'
        self.sales_incentive = sales_incentive

    def getpay(self) -> float:
        return super().getpay() + self.sales_incentive

    def __str__(self) -> str:
        return f'SalesEmployee{self.__dict__}'


def show_example_01():
    emp1: Employee = SalesEmployee('John Wick', 1_000_000, 10_000, 1000)
    print(f'Total payment: ${emp1.getpay():,.2f}')


def main():
    show_example_01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
