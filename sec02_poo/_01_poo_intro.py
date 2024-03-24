"""CLASES

Todo en python es un objeto, que se genera a partir de modelos denominados
clases.

Una clase otorga comportamineto y estado a cada uno de las instancias que
se generen a partir de estas. Dada una clase C, generamos una instancia
de la forma

objeto =  C()

donde objeto podrá acceder a sus miembros de instancia y miembros de clase.

Podemos agregar propiedades de instancia a un objeto de forma dinámica,
aunque estás solo existirán en objetos concretos y no serán compartidos
por las demás instancias.
"""


class Person:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, it's {self.name}")


def runtimeType(obj: object) -> str:
    return str(type(obj))[8:-2]


def showExample01():
    p1 = Person('John Wick', 45)
    p1.job = 'Killer'

    # agregamos función dinámica clase.
    Person.show_job = lambda p: print(p.job)
    Person.show_job(p1)
    print(runtimeType(Person.show_job))

    # invocamos método de instancia
    p1.greet()
    print(p1.__dict__)
    print(Person.__dict__)


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
