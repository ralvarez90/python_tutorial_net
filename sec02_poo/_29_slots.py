"""SLOTS

Los slots o ranuras permiten implementar clases más eficientes en
memoria. 

Recordemos que por default cada instancia de una clase tiene su propio
diccionario __dict__ que almacena todas sus variables de instancia.

Las instancias que sean de una clase con slots no tiene  asignada la
propiedad __dict__ que almacena las variables de instancia de su estado
propio.

No podrá agregar atributos de forma dinámica ya que no existe el atributo
__dict__ donde almacenarlos. Si puede agregar varibles de clase de forma
dinámica.
"""
from random import randint
from time import perf_counter


class Point2DV1:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'


class Point2DV2:
    __slots__ = ('x', 'y')

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'


def show_example_01():
    coordenadas = []
    point = Point2DV1(0, 0)
    print(point)
    print(point.__dict__)

    # generamos 1_000_000 instancias con coordenadas
    # aleatorias con valores entre el -10000 y 10000
    ti = perf_counter()
    for i in range(1_000_000):
        coordenadas.append(
            Point2DV1(x=randint(-1_000_000, 1_000_000), y=randint(-1_000_000, 1_000_000)))
    tf = perf_counter()
    delta_t = tf-ti
    print(f'Tiempo estimado: {delta_t:.2f} seg')


def show_example_02():
    coordenadas = []
    point = Point2DV2(0, 0)

    # generamos 1_000_000 instancias con coordenadas
    # aleatorias con valores entre el -10000 y 10000
    ti = perf_counter()
    for i in range(1_000_000):
        coordenadas.append(
            Point2DV2(x=randint(-1_000_000, 1_000_000), y=randint(-1_000_000, 1_000_000)))
    tf = perf_counter()
    delta_t = tf-ti
    print(f'Tiempo estimado: {delta_t:.2f} seg')


def main():
    show_example_01()
    show_example_02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
