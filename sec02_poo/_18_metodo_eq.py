"""MÉTODO __eq__

Se emplea para establecer el comportamiento al comprar dos objetos con
el operador  ==.

Si se comparan dos objetos usando ==, por default python utiliza el
operador is para determinar si son 'iguales'. Este comportamiento
se sobrescribe implementando el dunder method __eq__.

Recordemos que is compara las referencias, es decir sirve para saber
si dos objetos tiena o apuntan a la misma referencia.
"""


class Person:

    def __init__(self, firstname: str, lastname: str, age: int) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __eq__(self, __other: object) -> bool:
        if isinstance(__other, Person):
            return self.firstname == __other.firstname and self.lastname == __other.lastname and self.age == __other.age
        return False


def show_example_01():
    p1 = Person('John', 'Doe', 45)
    p2 = Person('John', 'Doe', 45)
    print(f'p1 is p2: {p1 is p2}')
    print(f'p1 == p2: {p1 == p2}')


def main():
    show_example_01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
