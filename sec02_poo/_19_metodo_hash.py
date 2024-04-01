"""MÉTODO __hash__

El método hash en Python se utiliza para generar un valor hash 
(o código hash) para un objeto. 

Un hash es un valor numérico único que se calcula a partir de los 
datos de un objeto y se utiliza principalmente para indexar y 
buscar en estructuras de datos como diccionarios. 

El método hash() es una función incorporada en Python que puede 
aplicarse a objetos inmutables, como cadenas, números y tuplas, 
para generar un valor hash.

Por otro lado, el método __hash__ es un método especial en Python 
que se utiliza para personalizar el cálculo del hash de un objeto. 
Si una clase define el método __hash__, este se llama cuando se 
utiliza la función hash() en una instancia de esa clase. 

Si sobrescribe el método __eq__ en una clase, esta generará
instancias unhasheables, por lo que no podrán ser usados como llaves
de diccionarios, en conjuntos, etc. En este caso deberá implementar
el método __hash__.
"""


class Person:
    """Clase que genera instancias inmutables de Personas.
    """

    def __init__(self, name: str, age: int) -> None:
        assert name != '' and age >= 0, 'Name cannot be an empty string and age cannot be a negative integer.'
        self._name = name
        self._age = age

    @property
    def age(self) -> int:
        return self._age

    @property
    def name(self) -> str:
        return self._name

    def __hash__(self) -> int:
        return hash((self._name, self._age))

    def __eq__(self, __other: object) -> bool:
        return isinstance(__other, Person) and self._name == __other._name and self._age == __other._age

    def __str__(self) -> str:
        return f'Person{self.__dict__} with hash: {hash(self)}'


def show_example_01():
    p1 = Person('John Wick', 45)
    p2 = Person('John Wick', 45)
    print(p1)
    print(p2)

    # si no existe __eq__ retorna false
    print(p1 == p2)

    # si no existe __hash__
    no_repeat_person = {p1, p2}
    for p in no_repeat_person:
        print(p)


def show_example_02():
    john_doe: Person = Person('John Doe', 33)
    print(john_doe.name)
    print(john_doe.age)
    print(john_doe)


def main():
    show_example_01()
    show_example_02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue. . .')
