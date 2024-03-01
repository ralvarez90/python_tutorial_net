"""MÉTODO __init__

Método que se invoca cuando inmediatemente después de crear
una instancia de alguna clase. Esta se encarga de otorgar o
inicializar el estado de cada objeto. Los métodos dunder 
indican que python los usa de forma interna.


Implementamos el método __init__ para inicializar variables
de la instancia.

Cuando crea un objeto ocurren dos cosas, primero se crea
una instancia estableciendo su propio namespace como un
diccionario __dict__ vacio y posteriormente invoca el método
__init__.

El método __init__ no es el constructor, este solo se encarga
de otorgar el estado inicial.
"""


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def show_namespace_dict(self):
        print(self.__dict__)


# run application
if __name__ == '__main__':

    # ejemplo 1
    person = Person('John Wick', 25)
    print(f'I am {person.name}. I am {person.age} years old')

    # ejemplo 2
    person.show_namespace_dict()

    # end message
    input('\nPress any key to continue . . .')
