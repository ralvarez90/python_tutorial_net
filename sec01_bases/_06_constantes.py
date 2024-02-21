"""CONSTANTES

Son objetos que permanecerán con su mismo estado durante
la ejecución del programa. Por convensión sus nombres son
en mayúsculas.

En python no existe un mecanismo de para definir constantes,
pero por la convensión anterior se asumen como constantes.
"""
from enum import Enum, auto

# string de formato
WELCOME_MESSAGE_FORMAT = 'Welcome {} {}!'


class Gender(Enum):
    """
    Representa todos los posibles géneros de una persona.
    """
    MALE = auto()
    FEMALE = auto()
    OTHER = auto()


def showWelcomeMessage(username: str, gender: Gender = Gender.OTHER):
    prefix = 'Mr.' if gender is Gender.MALE else 'Ms.' if gender is Gender.FEMALE else ''
    print(WELCOME_MESSAGE_FORMAT.format(prefix, username))


if __name__ == '__main__':

    # se ingresa nombre
    name = input('name1: ')
    showWelcomeMessage(name)

    # se establece genero masculino
    showWelcomeMessage('Rodrigo', Gender.MALE)

    # end application
    input('\nPress any key to continue . . . ')
