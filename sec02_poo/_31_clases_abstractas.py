"""CLASES ABSTRACTAS

Clases cuyo objetivo es que sean extendidas por otras clases. Las
clases asbtractas no pueden ser instanciadas mienstras que las
clases derivadas que sean concretas si.

De forma típica una clase abstracta está diseñada para crear
moldes de diseño de otras clases. Una clase abstracta es aquella
que al menos incluye un método abstracto.

Un método abstracto es aquel que se declara pero no se implementa. Es
decir no tiene una definición 'completa'.

Empleamos el módulo abc para crear clases abstractas y métodos
abstractos.

En la práctica, se utilizan clases abstractas para compartir el 
código entre varias clases estrechamente relacionadas.
"""
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

    @property
    def fullname(self) -> str:
        return f'{self.firstname} {self.lastname}'

    @abstractmethod
    def getsalary(self):
        pass


class FulltimeEmployee(Employee):
    def __init__(self, firstname: str, lastname: str, salary: float) -> None:
        super().__init__(firstname, lastname)
        self.salary = salary

    def getsalary(self):
        return self.salary


class HourlyEmployee(Employee):
    def __init__(self, firstname: str, lastname: str, worked_hours: int, rate: float) -> None:
        super().__init__(firstname, lastname)
        self.worked_hours = worked_hours
        self.rate = rate

    def getsalary(self):
        return self.worked_hours * self.rate


class Payroll:
    def __init__(self) -> None:
        self.employees: list[Employee] = []

    def add(self, employee: Employee) -> 'Payroll':
        self.employees.append(employee)
        return self

    def print(self):
        for e in self.employees:
            print(f'{e.fullname} \t ${e.getsalary():,.2f}')


def showExample01():
    payroll = Payroll()
    payroll \
        .add(FulltimeEmployee('John1', 'Wick1', 100_000)) \
        .add(FulltimeEmployee('John2', 'Wick2', 150_000)) \
        .add(HourlyEmployee('John3', 'Wick3', 35, 8000))  \
        .add(HourlyEmployee('John4', 'Wick4', 32, 8500))  \
        .add(HourlyEmployee('John5', 'Wick5', 39, 7600))  \

    # show data
    payroll.print()


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
