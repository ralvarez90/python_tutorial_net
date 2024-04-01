"""METACLASES

Ejemplo completo.
"""
from pprint import pprint


class Human(type):
    def __new__(mcls, name: str, bases: dict, class_dict: dict):
        selfclass = super().__new__(mcls, name, bases, class_dict)
        selfclass.freedom = True
        return selfclass


class Person(object, metaclass=Human):
    def __init__(self, name: str, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'Person{self.__dict__}'


def show_example_01():
    p = Person('John Wick', 45)
    print(p)
    print(f'Person.freedom: {Person.freedom}')


def main():
    show_example_01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
