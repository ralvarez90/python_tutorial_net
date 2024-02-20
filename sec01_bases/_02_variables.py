"""VARIABLES

Las variables son nombres identificadores a los cuales se les
asigna un valor, asociando dicho nombre a dicho valor.

La forma en la que se declara una variable es:
nombre_variable = valor
"""


def showMessage():
    message: str = 'Hello World in Python3'
    print(f'message: {message}')


if __name__ == '__main__':

    # imprime mensaje
    showMessage()

    # end message
    input('\nPress any key to continue . . . ')
