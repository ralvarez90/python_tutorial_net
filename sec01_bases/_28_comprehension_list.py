"""LISTAS POR COMPRENSIÓN

Tanto la función for loop como map() pueden ayudarle a crear una 
nueva lista basada en una existente.

Las list comprehension nos permite generar listas a partir de
expresiones. Se pueden agregar condiciones.
"""


def example_list_comprehensions1():
    numbers = [1, 2, 3, 4, 5]
    squares = [n**2 for n in numbers]
    print(f'numbers: {numbers}')
    print(f'squares: {squares}')


def example_list_comprehensions2():
    mountains = (
        ['Malaku', 8485],
        ['Lhotse', 8516],
        ['Kanchendzonga', 8586],
        ['K2', 8611],
        ['Everest', 8848],
    )
    higuests_v1 = list(filter(lambda m: m[1] > 8600, mountains))
    higuests_v2 = [m for m in mountains if m[1] > 8600]
    print(f'higuest_v1: {higuests_v1}')
    print(f'higuest_v2: {higuests_v2}')


def main():
    # run examples
    example_list_comprehensions1()
    example_list_comprehensions2()


if __name__ == '__main__':

    # run application
    main()

    # end message
    input('\nPress any key to continue . . . ')
