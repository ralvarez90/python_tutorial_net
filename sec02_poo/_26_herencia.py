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

    def __init__(self, name: str):
        self.name = name

    def greet(self) -> str:
        return f'Hi, it is {self.name}'

    def __str__(self) -> str:
        return f'Person{self.__dict__}'


class Employee(Person):
    """Clase Empleado que cumple la relación 'es una' Persona.
    """

    def __init__(self, name: str, jobTitle: str):
        super().__init__(name)
        self.jobTitle = jobTitle

    def __str__(self) -> str:
        return f'Employee{self.__dict__}'


def showExample01():
    employee1 = Employee(name='John Wick', jobTitle='Killer')
    person1 = Person('Juan Güic')
    print(f'employee1: {employee1}')
    print(f'person1  : {person1}')


def showExample02():
    e1 = Employee(name='Peter Parker', jobTitle='Super hero')
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
