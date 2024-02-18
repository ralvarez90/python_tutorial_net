"""ATRIBUTOS
"""
from pprint import pprint
import json


class Person:

    __counter: int = 0

    def __init__(self, name: str, age: int) -> None:
        Person.__counter += 1
        self.name = name
        self.age = age
        self.otro = {
            'cp': 15900,
            'url': 'localhost',
            'isAlive': None,
        }

    def getTotalPersons():
        return Person.__counter


if __name__ == '__main__':

    # instancia
    p1 = Person('John Wick', 33)
    print(json.dumps(p1.__dict__))

    # total de personas
    print(Person.getTotalPersons())

    pprint(p1.__dict__)
    pprint(Person.__dict__)
