"""CLASE TYPE

Recordemos que en python las clases también son objetos, por lo que
son instancias de una clase, dicha clase es type. Esto quiere decir
que las clase son instancias de type.

Python usa la clase de tipo para crear otras clases. La clase type en sí es 
invocable. A continuación se muestra uno de los constructores de esta clase:
type(name, bases, dict) -> a new type

Técnicamente, puedes usar la clase de tipo para crear una clase 
dinámicamente. Antes de hacerlo, debes comprender cómo Python 
crea las clases.

Cuando el intérprete de Python encuentre una definición de clase 
en el código, hará lo siguiente:

- Primero, extrae el cuerpo de la clase como una cadena.
- En segundo lugar, crea un diccionario de clases para el 
espacio de nombres de la clase.
- En tercer lugar, ejecute el cuerpo de la clase para llenar el 
diccionario de la clase.
- Finalmente, cree una nueva instancia de tipo usando el constructor type()
anterior.
"""


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def greeting(self):
        return f'Hi, I am {self.name}. I am {self.age} years old.'


def showExample01():
    print(f'type(Person) -> {type(Person)}')
    print(f'isinstance(Person, type) -> {isinstance(Person, type)}')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
