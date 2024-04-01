"""MÉTODO __str__

Permite retornan un string representativo de un determinado objeto.
El comportamiento default se sobrescribe implementando este dunder
métod dentro de la clase correspondiente.
"""


class Person:

    def __init__(self, firstname: str, lastname: str, age: int) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self) -> str:
        return f'Person{self.__dict__}'


def show_example_01():
    person = Person('John', 'Wick', 45)
    print(person)


def main():
    show_example_01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
