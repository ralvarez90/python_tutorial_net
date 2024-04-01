"""DATA CLASSES

Se introducen en la versión 3.7. Permiten definir clases de forma
más fácil y con funcionalidad out of the box. Básicamente permite
crear clases y establecer ciertos métodos dunder por defecto.

Se emplea el decorador @dataclass para crear una clase con estas
características. Los parámetros con valor default inicial assignado
deberán ir al último después de los que no tienen valor asignado.

El módulo dataclasses contiene funciones llamados astuple asdict que 
recibe una instancia de dataclass.

Las dataclasses nos ofrecen la posibilidad de generar objetos
inmutables, es decir de sodo ledctiras. Esto se establece empleando
el parámetro frozen en el decorador @dataclass

Si desea usar metaclases pero no requiere inicializar un campo
mediante un argumento de __init__ puede usar la función field de
mismo módulo dataclasses. Requiere implementar __post_init__.
"""
from dataclasses import dataclass, asdict, astuple, field


@dataclass
class Person:
    name: str
    age: int
    iq: int = 100
    can_vote: bool = field(init=False)

    def __post_init__(self):
        self.can_vote = 18 <= self.age <= 70


@dataclass(frozen=True)
class Persona:
    nombre: str
    edad: int
    iq: int = 123


def show_example_01():
    p = Person(name='John Wick', age=34)
    print(p)


def show_example_02():
    p1 = Person('name', 0)
    p2 = Person('name', 0)
    print(p1, p1.__dict__)
    print(p2, p2.__dict__)
    print(p1 == p2)


def show_example_03():
    some_person = Person(name='John Wick', age=45, iq=2000)
    some_person.can_vote = True
    print(some_person)
    print(astuple(some_person))
    print(asdict(some_person))


def show_example_04():
    readonly_person = Persona(nombre='Juan Wick', edad=34)
    print(readonly_person)


def main():
    show_example_01()
    show_example_02()
    show_example_03()
    show_example_04()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
