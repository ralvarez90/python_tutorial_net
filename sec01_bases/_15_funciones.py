"""FUNCIONES

Son bloques de código reutilizables que regresan un valor. Si no se 
especifica el valor a retornar con una sentencia return, se retorna 
un None de forma implícita.

Python incluye funciones built-in listas para usar.
"""


def agradecer():
    """Display a greeting to users."""
    print('Hi')


if __name__ == '__main__':

    # invocamos función
    agradecer()

    # end message
    input('\nPress any key to continue . . . ')
