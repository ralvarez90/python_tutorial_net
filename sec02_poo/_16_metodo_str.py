"""MÉTODO __str__

Permite retornan un string representativo de un determinado objeto.
El comportamiento default se sobrescribe implementando este dunder
métod dentro de la clase correspondiente.
"""


class Person:

    def __init__(self, firstName: str, lastName: str, age: int) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def __str__(self) -> str:
        return f'Person{self.__dict__}'


def showExample01():
    person = Person('John', 'Wick', 45)
    print(person)


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
