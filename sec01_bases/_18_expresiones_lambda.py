"""EXPRESIONES LAMBDA

Son funciones anónimas sue suelen tener solo una expresión como cuerpo. Se
pueden asignar a nombres de variables.

La sintaxis es:
lambda parameters: expression

Una función puede retornar otra, por lo que para este fin de igual forma se
pueden emplear las expresiones lambdas.
"""


def showExample01():
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
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
