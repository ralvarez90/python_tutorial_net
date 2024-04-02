"""DATACLASES 

Recordemos que podemos tener dataclasses que generarn
instancias inmutables usando el parámetro froze, usar
los métodos astuple y asdict con las instancias, o
establecer campos que no se inicializen en el constructor
usando la función field y el método __post_init.

El atributo order=True permite establecer que los objetos
instancias de dataclass sean comparables. 

En Resumen:
- Utilice el decorador @dataclass del módulo dataclasses para convertir una clase 
en una clase de datos. El objeto de clase de datos implementa __eq__ y __str__ 
de forma predeterminada.

- Utilice las funciones astuple() y asdict() para convertir un objeto de una 
clase de datos en una tupla y un diccionario.

- Utilice frozen=True para definir una clase cuyos objetos sean inmutables.

- Utilice el método __post_init__ para inicializar atributos que dependen 
de otros atributos.

- Utilice sort_index para especificar los atributos de clasificación de los 
objetos de clase de datos.
"""
from dataclasses import dataclass, field


@dataclass(order=True)
class Person:
    sort_index: int = field(init=False, repr=False)

    name: str
    age: int
    can_vote: bool = field(init=False)

    def __post_init__(self):
        self.can_vote = 18 <= self.age <= 70
        self.sort_index = self.age


def show_example_01():
    members = [
        Person(name='John1', age=31),
        Person(name='John2', age=32),
        Person(name='John3', age=33),
        Person(name='John4', age=34),
        Person(name='John5', age=29),
    ]
    sorted_members = sorted(members)
    for member in sorted_members:
        print(f'{member.name}(age={member.age})')


def main():
    show_example_01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
