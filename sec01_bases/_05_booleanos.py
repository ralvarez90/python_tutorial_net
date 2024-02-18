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
    def checkStatus(user: 'User'):
        if user.isActive:
            print('OK')
            return
        print('ERROR')


if __name__ == '__main__':

    # instances
    userAdmin = User('Rodrigo Álvarez', Roll.ADMIN)
    otherUser = User('Aldo Caldo', Roll.NORMAL)
    otherUser.deactivate()

    # status 1
    User.checkStatus(userAdmin)

    # status 2
    User.checkStatus(otherUser)

    # end application
    input('\nPress any key to continue . . . ')
