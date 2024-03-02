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

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, __other: object) -> bool:
        if isinstance(__other, Person):
            return self.first_name == __other.first_name and self.last_name == __other.last_name and self.age == __other.age
        return False


def show_example_1():
    p1 = Person('John', 'Doe', 45)
    p2 = Person('John', 'Doe', 45)
    print(f'p1 is p2: {p1 is p2}')
    print(f'p1 == p2: {p1 == p2}')


def main():
    show_example_1()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . .')
