"""DESCRIPTORS

En python un descriptor es protocolo que permite a los objetos
personalizar cómo se accede, asiga y elimina un valor en sus
atributos.

Un descriptor es una clase que implementa al menos
uno de los siguientes métodos especiales:
__get__(self, instance, owner)
__set__(self, instance, value)
__set_name__(self, instance, owner)
__delete__(self, instance)

Los descriptores se utilizan comúnmente en Python para crear 
propiedades, métodos estáticos y métodos de clase. Son especialmente 
útiles cuando quieres tener un control adicional sobre cómo se accede 
o modifica un atributo de una clase.

todo agregar mas notas sobre descriptores
"""


class Descriptor:

    def __init__(self, value) -> None:
        self._value = value

    def __get__(self, instance, owner):
        print('Accediendo al valor')
        return self._value

    def __set__(self, instance, value):
        print('Asignando valor')
        self._value = value


class RequiredString:
    def __set_name__(self, owner, name):
        self.propertyName = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.propertyName] or None

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'The {self.propertyName} must be a string')
        if len(value) == 0:
            raise ValueError(f'The {self.propertyName} cannot be empty')
        instance.__dict__[self.propertyName] = value


class Person:
    firstname = RequiredString()
    lastname = RequiredString()


class MyClase:
    descriptor = Descriptor("initial descriptor")


def showExample01():
    obj = MyClase()
    print(obj.descriptor)
    obj.descriptor = 'new descriptor'
    print(obj.descriptor)


def showExample02():
    try:
        p = Person()
        p.firstname = ''
    except ValueError as e:
        print(e)


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
