"""FUNCIÓN MAP

Cuando se trabaja con una lista (o una tupla), a menudo es necesario 
transformar los elementos de la lista y devolver una nueva lista 
que contenga el elemento transformado. Para esto se emplea la
función map, que recibe una función que se invocará por cada
uno de los elementos del iterable que reciba como argumento.

La función que recibe como primer argumento puede ser externa o una
expresión lambda.

La función asignada al parámetro de map recibe solo un parámetro y
regresa solo 1 valor.
"""


Number = int | float | complex


def getSquare(number: Number) -> Number:
    return number ** 2


def showExample01():
    bonuses = [100, 200, 300]
    doubles = list(map(lambda x: x*2, bonuses))
    squares = list(map(getSquare, bonuses))
    negatives = list(map(lambda n: -n, bonuses))
    print(f'bonuses  : {bonuses}')
    print(f'doubles  : {doubles}')
    print(f'squares  : {squares}')
    print(f'negatives: {negatives}')


def showExample02():
    names = ['david', 'peter', 'jenifer']
    titleFormatNames = list(map(lambda name: name.title(), names))
    print(f'names: {names}')
    print(f'titleFormatNames: {titleFormatNames}')


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
