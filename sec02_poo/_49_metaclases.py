"""METACLASES

Una metaclase es una clase que se utiliza para crear una clase. Python
usa la metaclase type para crear otras clases.

Python usa la metaclase type para crear clases por default. El argumento 
metaclass permite especificar qué clase de metaclase usar para definir 
la clase. Por lo tanto, puedes crear una metaclase personalizada que 
tenga su propia lógica para crear otras clases. 

Al utilizar una metaclase personalizada, puede inyectar funcionalidad 
en el proceso de creación de clases. Para crear una metaclase personalizada
podemos extender a la metaclase type.
"""


class Human(type):
    """Metaclase Human, que exitende a type.
    """
    def __new__(cls, name: str, bases: tuple, class_dict: dict):
        class_ = super().__new__(cls, name, bases, class_dict)
        class_.freedom = True
        return class_


class Person(object, metaclass=type):
    """Clase concreta con definición explícita. Extiende a object y usa type como metaclase.
    """

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'Person{self.__dict__}'


class Persona(object, metaclass=Human):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'Persona{self.__dict__}'


def showExample01():
    """Instancia de clase normal que usa como metaclase type.
    """
    p = Person('John Wick', 45)
    print(p)


def showExample02():
    """Instancía de case que usa metaclase personalizaa"""
    p = Persona(name='John Wick', age=34)
    print(p)


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
