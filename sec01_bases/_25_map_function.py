"""FUNCIÓN MAP

Cuando se trabaja con una lista (o una tupla), a menudo es necesario 
transformar los elementos de la lista y devolver una nueva lista 
que contenga el elemento transformado. Para esto se emplea la
función map, que recibe una función que se invocará por cada
uno de los elementos del iterable que reciba como argumento.

La función que recine como primer argumento puede ser externa o una 
expresión lambda.
"""


def square(number: int | float) -> int | float:
    return number**2


def show_example_1():
    bonuses = [100, 200, 300]
    doubles = list(map(square, bonuses))
    negatives = list(map(lambda n: -n, bonuses))
    print(f'bonuses  : {bonuses}')
    print(f'doubles  : {doubles}')
    print(f'negatives: {negatives}')


def show_example_2():
    names = ['david', 'peter', 'jenifer']
    title_names = list(map(lambda name: name.title(), names))
    print(f'names: {names}')
    print(f'title_names: {title_names}')


def main():
    show_example_1()
    show_example_2()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . . ')
