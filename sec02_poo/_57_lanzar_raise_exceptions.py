"""LANZAR EXCEPCIONES

La sentencia raise permite lanzar excepciones, es como el throws en java.
La sintaxis es de la forma
raise ExceptionType() donde esta es una subclase de BaseException.

Es posible relanzar la excepción en si desde su mismo bloque except.
"""


def showExample01():
    try:
        raise ValueError('The value error exception', 'x', 'y')
    except ValueError as e:
        print(e)
        print(e.args)


def showExample02():
    def division(a, b):
        try:
            return a/b
        except ZeroDivisionError as e:
            print(f'Loggin exception: ', str(e))
            raise
    division(1, 0)


def main():
    showExample01()
    # show_example_02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
