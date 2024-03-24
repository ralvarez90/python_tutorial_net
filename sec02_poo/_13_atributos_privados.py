"""ATRIBUTOS PRIVADOS

La encapsulación es uno de los pilares de la POO junto con
la abstracción, herencia y polimorfismo.

Python no soporta establecer miembros privados dentro de 
una clase pero por convensión se emplea el _ y el __ para
indicar que cierta variable de instancia, clase o métodos
serán privados y solo se utilizarán dentro de su respectiva
clase.

Si empleamos el prefijo __ python renombre el nombre del 
atributo de la forma _nombreDeClase__nombreCampo simulando
de mejor forma el ocultamiento de atributos o métodos dentro
de una clase. Esta característiza se denomina 'name mangling'.
"""


class Counter:

    def __init__(self) -> None:
        self.current = 0

    def increment(self) -> 'Counter':
        self.current += 1
        return self

    def value(self) -> int:
        return self.current

    def reset(self):
        self.current = 0


class Contador:

    def __init__(self) -> None:
        self._current = 0

    def increment(self) -> 'Contador':
        self._current += 1
        return self

    def valor(self) -> int:
        return self._current

    def reset(self):
        self._current = 0


def showExample01():
    # generamos instancia
    counter = Counter()
    counter.increment()
    counter.increment()
    counter.current = 123  # esto no debe de ser
    print(f'counter.value() -> {counter.value()}')


def showExample02():
    contador = Contador()
    contador.increment()
    contador.increment()
    contador.increment()
    contador.reset()
    print(f'contador.valor() -> {contador.valor()}')


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue. . .')
