"""ATRIBUTOS

Son campos dentro de una clase. Puede haber de instancias o de clase.
"""
import json
from pprint import pprint


class Person:
    # atributo privado de clase
    _counter: int = 0

    # initial state
    def __init__(self, name: str, age: int) -> None:
        Person._counter += 1
        self.name = name
        self.age = age
        self.otro = {
            'cp': 15900,
            'url': 'localhost',
            'isAlive': None,
        }

    # función dentro de una clase
    def getTotalCountPersons():
        return Person._counter


def showExample01():
    # instancia
    p1 = Person('John Wick', 33)
    print(json.dumps(p1.__dict__))

    # total de personas
    print(Person.getTotalCountPersons())

    pprint(p1.__dict__)
    pprint(Person.__dict__)


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
