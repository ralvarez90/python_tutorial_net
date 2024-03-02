"""MÉTODO __del__

El recolector de basura se encarga de gestionar la memoria. Cuando
tenemos un objeto no referenciado a ninguna variable, se invoca el 
recolector de basura.

El método __del__ de un objeto se invoca justo antes de que el recolector
de basura elimine el objeto.

El recolector de basura determina cuando eliminar un objeto por lo tanto
de el depende el cuándo se invocará el método __del__.

No se recomienda usar el método __del__ para cerrar o eliminar recursos, 
siempre es mejor usar manejadores de contexto.

Si existe una exepción dentro del método __del__ se lanza de manera
silenciosa.

Si emplea la palabra reservada del objeto entonces se invoca de forma
inmediata el método __del__.
"""


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __del__(self):
        print('__del__ was called...')


def run_example():
    p1 = Person('John Wick', 45)
    p1 = None
    p2 = Person('Juan Güic', 45)
    del p2


def main():
    run_example()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . .')
