"""FUNCIONES

Son bloques de código reutilizables que regresan un valor. Si no se 
especifica el valor a retornar con una sentencia return, se retorna 
un None de forma implícita.

Python incluye funciones built-in listas para usar.
"""


def agradecer():
    """Display a greeting to users."""
    print('Nos salvaste, estamos agradecidos')


def say_hi():
    print('Hi!')


def show_example_01():
    say_hi()
    agradecer()


def main():
    show_example_01()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . . ')
