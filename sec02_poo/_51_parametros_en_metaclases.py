"""PARÁMETROS EN METACLASES

Para pasar parámetros a metaclases empleamos argumentos kwargs.

Aquí está la cita de Tim Peter, quien escribió el Zen de Python:

Las metaclases son magia más profunda y el 99% de los usuarios nunca 
deberían preocuparse por ellas. Si se pregunta si los necesita, 
no es así (las personas que realmente los necesitan saben con certeza 
que los necesitan y no necesitan una explicación sobre por qué).

En la práctica, a menudo no es necesario utilizar metaclases a menos 
que mantengas o desarrolles el núcleo de marcos grandes como Django.
"""


class Human(type):
    """Some metaclass."""
    def __new__(mcls, name, bases, class_dict, **kwargs):
        class_ = super().__new__(mcls, name, bases, class_dict)
        if kwargs:
            for name, value in kwargs.items():
                setattr(class_, name, value)
        return class_


class Person(object, metaclass=Human, country='MX', freedom=True):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def show_example_01():
    print(Person.__dict__)


def main():
    show_example_01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
