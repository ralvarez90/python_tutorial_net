"""PRINCIPIO DE SEGREGACIÓN DE INTERFACES

Recordemos que una interfaz es una descripción de comportamientos que 
un objeto puede realizar. En programación orientada a objetos, una 
interfaz es un conjunto de métodos que un objeto debe tener. 

El propósito de las interfaces es permitir a los clientes solicitar 
los métodos correctos de un objeto a través de su interfaz.

Python utiliza clases abstractas como interfaces porque sigue el 
llamado duck typing. El principio de duck typing establece que 
“si camina como un pato y grazna como un pato, debe ser un pato”. 

En otras palabras, los métodos de una clase determinan cuáles serán 
sus objetos, no el tipo de clase.

El principio de segregación de interfaces establece que una interfaz 
debe ser lo más pequeña posible en términos de cohesión. En otras palabras, 
debería hacer UNA cosa.

No significa que la interfaz deba tener un método. Una interfaz puede 
tener múltiples métodos cohesivos.

# todo agregar ejemplo
"""
from abc import ABC, abstractmethod


class Movable(ABC):
    @abstractmethod
    def go(self):
        pass


class Flyable(Movable):
    @abstractmethod
    def fly(self):
        pass


class Aircraft(Flyable):
    def go(self):
        print('Going...')

    def fly(self):
        print('Flying...')


class Car(Movable):
    def go(self):
        print('Going...')
