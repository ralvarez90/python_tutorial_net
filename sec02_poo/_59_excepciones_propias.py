"""CUSTOM EXCEPTIONS

Para crear excepciones propias puede definir su clase propia 
extendiendo a Exception.

Como a cualquier otra clase, podemos añadirles funcionalides
como propiedades y métodos.

En la práctica, querrás mantener organizadas las excepciones 
personalizadas creando una jerarquía de excepciones personalizada. 

La jerarquía de excepciones personalizada le permite detectar 
excepciones en múltiples niveles, como las clases de excepción 
estándar.
"""


class FahrenheitError(Exception):
    min_f = 32
    max_f = 212

    def __init__(self, f: float,  *args: object) -> None:
        super().__init__(args)
        self.f = f

    def __str__(self) -> str:
        return f'The {self.f} is not in a valida range {self.min_f, self.max_f}'


def show_example_01():
    pass


def main():
    show_example_01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
