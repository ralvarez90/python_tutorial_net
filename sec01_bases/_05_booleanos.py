"""BOOLEANOS

Extienden de int y son instancias de bool. Permiten efectuar operacioes
booleanas y solo pueden tener alguno de los siguientes valores True
o False.

1. Constructor bool
Este recibe cualquier objeto y retorna un booleano equivalente. Cualquier
objeto distinto de 0, '', None, [], {}, () retorna True.
"""
from enum import Enum


class Roll(Enum):
    ADMIN = 1
    NORMAL = 2


class User:
    """Representa un usuario.
    """

    def __init__(self, name: str, roll: Roll = Roll.NORMAL) -> None:
        """Inicializa el objeto de un tipo Usuario.
        """
        self.name = name
        self.roll = roll
        self.isActive = True

    def deactivate(self):
        assert self.isActive, 'The user is not active'
        self.isActive = False

    @staticmethod
    def checkstatus(user: 'User'):
        if user.isActive:
            print('OK')
            return
        print('ERROR')


def show_example_1():
    # instancias
    user1 = User('Rodrigo Álvarez', Roll.ADMIN)
    user2 = User('Aldo Caldo', Roll.NORMAL)

    # cambio de estado de user2
    user2.deactivate()

    # verificación de estatis
    User.checkstatus(user1)
    User.checkstatus(user2)


def main():
    show_example_1()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . . ')
