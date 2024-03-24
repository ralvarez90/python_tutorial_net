"""HERENCIA

Pilar de la POO que permite la reutilización de clases, extendiendo
la lógica existente dentro de una clase.

Cuando una clase B extiende a otra clase A, decimos que A herea a B.
Esto se denomina herencia simple. Dentro de una clase hija, accedemos
a la referencia de la clase padre empleando la palabra reservada
super.

Note que python soporta herencia múltiple. Podemos usar la función
isinstance para determinar si determinado objeto es instancia de una
o más clases.

Otro método de utilidad es el método issubclass, que permite saber si
una clase extiende de otra (u otras). Todos los objetos extienden de
la clase de object.
"""


class Person:
    """Clase con propiedad self.name y método.
    """

    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> str:
        return f'Hi, it is {self.name}'

    def __str__(self) -> str:
        return f'Person{self.__dict__}'


class Employee(Person):
    """Clase Empleado que cumple la relación 'es una' Persona.
    """

    def __init__(self, name: str, job_title: str) -> None:
        super().__init__(name)
        self.job_title = job_title

    def __str__(self) -> str:
        return f'Employee{self.__dict__}'


def showExample01():
    employee_1 = Employee(name='John Wick', job_title='Killer')
    person_1 = Person('Juan Güic')
    print(f'employee_1: {employee_1}')
    print(f'person_1  : {person_1}')


def showExample02():
    e1 = Employee(name='Peter Parker', job_title='Super hero')
    p1 = Person(name='Van Dame')
    print(f'e1 is a Person  : {isinstance(e1, Person)}  ')
    print(f'e1 is a Employee: {isinstance(e1, Employee)}')
    print(f'p1 is a Person  : {isinstance(p1, Person)}  ')
    print(f'p1 is a Employee: {isinstance(p1, Employee)}')


def showExample03():
    print(f'Employee issubclass of Person : {issubclass(Employee, Person)}')
    print(f'Person issubclass of Employee : {issubclass(Person, Employee)}')


def main():
    showExample01()
    showExample02()
    showExample03()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
