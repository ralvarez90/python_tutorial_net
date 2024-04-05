"""BOOLEANOS

Extienden de int y son instancias de bool. Permiten efectuar operaciones
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
    def checkStatus(user: 'User'):
        if user.isActive:
            print('OK')
            return
        print('ERROR')


def showExample01():
    # instancias
    user1 = User('Rodrigo Álvarez', Roll.ADMIN)
    user2 = User('Aldo Caldo', Roll.NORMAL)

    # cambio de estado de user2
    user2.deactivate()

    # verificación de estatus
    User.checkStatus(user1)
    User.checkStatus(user2)


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
