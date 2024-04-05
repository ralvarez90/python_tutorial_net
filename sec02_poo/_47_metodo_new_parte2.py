"""MÉTODO __new__

En el siguiente ejempo se define una clase Person y se crean
propiedades de dicho objeto de forma dinámica. Recordar que
normalmente, cuando anulas el método __new__(), no necesitas 
definir el método __init__() porque todo lo que puedes hacer 
en el método __init__(), puedes hacerlo en el método __new__().
"""


class Person:
    def __new__(cls, firstname: str, lastname: str):
        self = object.__new__(cls)
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = f'{self.firstname} {self.lastname}'
        return self

    def __str__(self) -> str:
        return f'Person{self.__dict__}'


def showExample01():
    p = Person('John', 'Wick')
    print(p.fullname)
    print(p)


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
