"""EXPRESIONES LAMBDA

Son funciones anónimas sue suelen tener solo una expresión como cuerpo. Se
pueden asignar a nombres de variables.

La sintaxis es:
lambda paramters: expression

Una función puede retorar otra, por lo que para este fin de igual forma se
pueden emplear las expresiones lambdas.
"""


def show_example():

    # declare and invoque in same line
    print(
        (lambda fname, lname: f'{fname}, {lname}')('Rodrigo', 'Álvarez')
    )

    # lista de funciones
    invocables = []
    for i in (1, 2, 3):
        invocables.append(lambda: i)

    # se invocan cad auna de las funciones almacendas.
    for f in invocables:
        print(f())


def main():
    show_example()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . . ')
