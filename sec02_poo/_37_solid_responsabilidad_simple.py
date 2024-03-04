"""PRINCIPIO DE RESPONSABILIDAD SIMPLE

Este es el primer principio SOLID. El SRP (Single Responsability Principle) mantiene
que toda clase, método y función solo debe cumplir una trabajo por hacer, o solo una
razón para cambiar.

El propósito de este principio es generar funciones, métodos y clases con alta cohesión
y bajo acomplamiento.

Promueve la composición de clases y evita el duplicar código. En resumen, el principio de 
responsabilidad simple (SRP) establece que cada clase, método o función debe tener 
solo un trabajo o una razón para cambiar.

Utilice el principio de responsabilidad simple para separar clases, métodos y 
funciones con el mismo motivo de cambio.
"""


class PersonDB:

    def save(self, person: 'Person'):
        print(f'Save the {person} to the database.')


class Person:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.db = PersonDB()

    def __repr__(self) -> str:
        return f'Person(name={self.name}, age={self.age})'

    def save(self):
        self.db.save(self)


def show_example_1():
    p = Person('John Wick', 45)
    print(p)
    db = PersonDB()
    db.save(p)


def show_example_2():
    p = Person('John Wick', 45)
    p.save()


def main():
    show_example_1()
    show_example_2()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . .')
