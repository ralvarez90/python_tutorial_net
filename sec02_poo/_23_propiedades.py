"""PROPIEDAES

Recordemos que dentro de las clases tenemoes variables de instancia y 
de clase. Estos de denominan miembros o campos.

1. Métodos setters y getters
Proveen dentro de las clase una interfaz para obtener o cambiar el estado
de variables de instancia.

En python existe un decorador llamado @property que permite establecer
variables de instancia que son funciones como si se tratasen de 
atributos que no son invocables.

2. Clase property
La clase property en Python es una herramienta que permite a los desarrolladores 
implementar y controlar el acceso, la asignación y la eliminación de atributos 
de una clase de una manera más controlada y flexible. Se utiliza para crear
propiedades gestionadas por métodos específicos para establecer, obtener y
eliminar valores de un atributos.
"""


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.__setage(age)

    def __setage(self, age: int):
        if age < 0:
            raise ValueError('The age cannot be a negative integer.')
        self.__age = age

    def __getage(self) -> int:
        return self.__age

    def __str__(self) -> str:
        return f'Person{self.__dict__}'

    # creamos propiedad
    age = property(fget=__getage, fset=__setage)


def show_example_1():
    john = Person('John Wick', 45)
    john.age = 35
    print(john)
    print(Person.__dict__)


def main():
    show_example_1()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . .')
