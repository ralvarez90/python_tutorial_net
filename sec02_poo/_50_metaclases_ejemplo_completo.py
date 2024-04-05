"""METACLASES

Ejemplo completo.
"""
from pprint import pprint


class Human(type):
    def __new__(cls, name: str, bases: dict, class_dict: dict):
        _class = super().__new__(cls, name, bases, class_dict)
        _class.freedom = True
        return _class


class Person(object, metaclass=Human):
    def __init__(self, name: str, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'Person{self.__dict__}'


def showExample01():
    p = Person('John Wick', 45)
    print(p)
    print(f'Person.freedom: {Person.freedom}')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
