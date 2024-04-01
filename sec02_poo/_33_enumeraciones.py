"""ENUMERACIONES

Una enumerasión es un conjunto de miembros asociados y bien acotados. Cada
miembro se asocia a un único valor constante. Python nos provee del módulo
enum y el tipo Enum para definir nuevas enumeraciones.

El campo de una enumeracion, digamos Enumeracion.CAMPO es una instancia de
Enumeracion.

Para verificar si un miembro dentro de un miembro está dentro de una enumeración
empleamos el operador in de la forma:
NombreEnumeracion.MIEMBRO in NombreEnumeracion

Podemos comparar dos miembros dentro de una enumeración con el operadpr ==
o con el operador de identidad is.

Los miembros dentro de una enumeración son hasheables, esto quiere decir
que podemos usar los miembros dentro de una enumeración como llaves en 
diccionarios o en conjuntos.

La forma típica de accesar a un miembro dentro de una enumeración es empleando
dot notation. Dado que Enum implementa el dunder method __getitem__, podemo acceer
a los miembros por medio de brackets [], ver ejemplo 5.

Las enumeraciones son objetos invocables (callables) por lo que podemos acceder
a cada uno de sus miembros por medio de sus valores, ver ejemplo 6.

Las enumeraciones son iterables por lo que podemos recorrer sus miembros por
medio del for, ver ejemplo 7. Puede emplear la clase list para retornar una 
lista con los miembros de una enumeración.

Las enumeraciones son inmutables. Y no podemos extender una enumeración que
no contenga miembros.
"""
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


def runtime_type(obj: object) -> str:
    return str(type(obj))


def show_example_01():
    print(runtime_type(Color))
    print(runtime_type(Color.RED))
    print(isinstance(Color.RED, Color))


def show_example_02():
    print(f'Color.RED.name  -> {Color.RED.name}')
    print(f'Color.RED.value -> {Color.RED.value}')


def show_example_03():
    if Color.RED in Color:
        print(
            f'El color {Color.RED} se encuentra dentro de la enumeración {Color}')

    if Color.RED is Color.BLUE:
        print(f'{Color.RED} is {Color.BLUE}')
    else:
        print(f'{Color.RED} is not {Color.BLUE}')


def show_example_04():
    rgb = {
        Color.RED: '#ff0000',
        Color.BLUE: '#00ff00',
        Color.GREEN: '#0000ff',
    }

    print(f'rgb dict: {rgb}')


def show_example_05():
    print(Color['RED'])
    print(Color['BLUE'])
    print(Color['GREEN'])


def show_example_06():
    print(Color(1))
    print(Color(2))
    print(Color(3))
    print(Color(1) is Color['RED'])  # true


def show_example_07():
    for color in Color:
        print(color, end=', ')
    print()
    colores = list(Color)
    print(colores)


def main():
    # run examples
    show_example_01()
    show_example_02()
    show_example_03()
    show_example_04()
    show_example_05()
    show_example_06()
    show_example_07()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
