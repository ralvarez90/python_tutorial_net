"""CONSTANTES

Son objetos que permanecerán con su mismo estado durante
la ejecución del programa. Por convensión sus nombres son
en mayúsculas.
"""
from enum import Enum, auto


WELCOME_MESSAGE_FORMAT = 'Welcome {} {}!'


class Gender(Enum):
    MALE = auto()
    FEMALE = auto()


def showWelcomeMessage(username: str, gender: Gender):
    prefix = 'Mr.' if gender is Gender.MALE else 'Ms.'
    print(WELCOME_MESSAGE_FORMAT.format(prefix, username))


if __name__ == '__main__':

    # get name
    name = input('name: ')

    # select gender
    showWelcomeMessage(name, Gender.MALE)

    # end application
    input('\nPress any key to continue . . . ')
