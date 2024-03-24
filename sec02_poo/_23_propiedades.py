"""PROPIEDADES

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

La clase property tiene los siguientes parámetros en su constructor
fget
    función que retorna el valor del atributo
fset
    función setter que establece el estado de un atributo
fdel
    función que elimina un atribito
doc
    Es un docstring
    
Al utilizar la clase property(), podemos agregar una propiedad a una 
clase manteniendo la compatibilidad con versiones anteriores. En la práctica, 
primero definirá los atributos. Más adelante, podrá agregar la propiedad a 
la clase si es necesario.
"""


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self._setAge(age)

    def _setAge(self, age: int):
        if age < 0:
            raise ValueError('The age cannot be a negative integer.')
        self.__age = age

    def _getAge(self) -> int:
        return self.__age

    def __str__(self) -> str:
        return f'Person{self.__dict__}'

    # creamos propiedad
    age = property(fget=_getAge, fset=_setAge)


def showExample01():
    john = Person('John Wick', 45)
    john.age = 35
    print(john)


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
