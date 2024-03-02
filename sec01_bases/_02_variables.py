"""VARIABLES

Las variables son nombres identificadores a los cuales se les
asigna un valor, asociando dicho nombre a dicho valor.

La forma en la que se declara una variable es:
nombre_variable = valor
"""


def show_example():
    message: str = 'Hello World in Python3'
    print(f'message: {message}')


def main():
    show_example()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . . ')
