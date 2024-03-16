"""CONSTANTES

Son objetos que permanecerán con su mismo estado durante
la ejecución del programa. Por conveniencia sus nombres son
en mayúsculas.

En python no existe un mecanismo de para definir constantes
son variables que simulan el comportamiento de las constantes
en otros lenguajes de programación.
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


def show_welcome_message(username: str, gender: Gender = Gender.OTHER):
    prefix = 'Mr.' if gender is Gender.MALE else 'Ms.' if gender is Gender.FEMALE else ''
    print(WELCOME_MESSAGE_FORMAT.format(prefix, username))


def show_example_01():
    # se ingresa nombre
    name = input('name1: ')
    show_welcome_message(name)

    # se establece género masculino
    show_welcome_message('Rodrigo', Gender.MALE)


def main():
    show_example_01()


if __name__ == '__main__':
    # run application
    main()

    # end application
    input('\nPress any key to continue . . . ')
