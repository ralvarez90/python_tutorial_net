"""FUNCIONES

Son bloques de código reutilizables que regresan un
valor. Si no se especifica el valor a retornar con
una sentencia return, se retorna un None de forma
implícita.

Python incluye funciones built-in listas para usar.
"""


def greet():
    """Display a greeting to users."""
    print('Hi')


if __name__ == '__main__':

    # call function
    greet()

    # end application
    input('\nPress any key to continue . . . ')
