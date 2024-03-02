"""MÉTODO __str__

Permite retornan un string representativo de un determinado objeto.
El comportamiento default se sobrescribe implementando este dunder
métod dentro de la clase correspondiente.
"""


class Person:

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self) -> str:
        return f'Person{self.__dict__}'


def show_example():
    person = Person('John', 'Wick', 45)
    print(person)


def main():
    show_example()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . .')
