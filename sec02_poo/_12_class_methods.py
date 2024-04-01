"""MÉTODOS DE CLASE

Recordemos que los métodos de instancia pueden acceder a variables de 
instancia dentro de la misma clase. Para invocar métodos de instancia, 
primero debe crear una instancia de la clase.

Cuando no se requiere crear instancias para invocar un método dentro
de una clase empleamos los métodos de clase.

Se emplea el decorador @classmethod para establecer que un método dentro
de una clase es de clase. Esto quiere decir que no se invoca desde
las instnacias.

Los métodos de clase reciben un atributo que hace referencia a la misma
clase contenedora. Esto nos permite acceder a las variables de instancia
de dicha clase. Por convensión ese parámetro se nombre cls.

Un método estático no puede acceder a las atributos de instancia. Pero
puede acceder a los atributos de clase via la variable cls, que es la 
referencia de la clase en cuestión.
"""


class Person:

    def __init__(self, firstName: str, lastName: str, age: int) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def get_fullname(self) -> str:
        return f'{self.firstName} {self.lastName}'

    def introduce(self):
        print(f"Hi. I'am {self.get_fullname()}. I'm {self.age} years old.")

    @classmethod
    def create_anonymous(cls):
        # print(f'type of cls: {type(cls)}') retorna type
        return Person('John', 'Doe', 44)


def show_example_01():
    """Invocando métodos de instancia
    """
    p = Person('Rodrigo', 'Álvarez', 33)
    p.introduce()
    Person.introduce(p)


def show_example_02():
    """Invocando métodos de clase.
    """
    p2 = Person.create_anonymous()
    p2.introduce()


def main():
    show_example_01()
    show_example_02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
