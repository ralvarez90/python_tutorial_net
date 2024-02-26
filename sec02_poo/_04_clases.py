"""CLASES

Los objetos son contenedores  de datos y funcionalidades. Los
datos representan el estado de un objeto en un determinado
tiempo. Los objetos emplen atributos para modelar dicho estado.

La funcionalidad de los objeto se implementa mediante los
métodos que son funiciones asociadas a determinados tipos
de objetos.

Empleamos la palabra reservada class para definir una determinada
clase y el nombreDeLaClase() para generar una instancia.

En Python todo es un objeto por lo que las clases también
son objetos, es decir son instancias de de clases.

Las clases son instancias de la clase type.
"""


class Person:
    pass


if __name__ == '__main__':

    # instancia y id
    p1 = Person()
    print(f'id(p1): {hex(id(p1))}')

    # propiedad __name__
    print(Person.__name__)
    print(isinstance(Person, type))
