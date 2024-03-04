"""PRINCIPIO OPEN-CLOSED

Este esel segundo principio SOLID, establece que cualquier método,
función debe permanecer abierta a la extensión y cerrada a la
modificación.

El proposito de este principio es hacer más fácil el agregar nuevas
características o casos de uso al sistema sin modificaar directamente
el código existente.
"""
import json
from abc import ABC, abstractmethod


class Person:

    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f'Person(name={self.name})'


class PersonStorage(ABC):
    @abstractmethod
    def save(self, person: Person):
        pass


class PersonDB(PersonStorage):
    def save(self, person: Person):
        print(f'Saving the {person} to database')


class PersonJSON(PersonStorage):
    def save(self, person: Person):
        print(f'Saving the {person} to a json file')


class PersonXML(PersonStorage):
    def save(self, person: Person):
        print(f'Saving the {person} to an xml file')


def show_example_1():
    pass


def main():
    show_example_1()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . .')
