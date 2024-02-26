"""ATRIBUTOS

Son campos dentro de una clase. Puede haber de instancia o de clase.
"""
from pprint import pprint
import json


class Person:

    # class attribute
    __counter: int = 0

    # initial state
    def __init__(self, name: str, age: int) -> None:
        Person.__counter += 1
        self.name = name
        self.age = age
        self.otro = {
            'cp': 15900,
            'url': 'localhost',
            'isAlive': None,
        }

    # función dentro de una clase
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
