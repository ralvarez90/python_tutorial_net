"""EXCEPCIONES

Son objetos de clases de excepciones. Todas las excepciones son
subclases de BaseException, sin embargo la mayoría de las excepciones
built-in de python extienden de Exception, que es a su vez una subclase
de BaseException.

Empleamos las excepciones por si se tiene bloques de código que puedan
generar errores, con la excepciones manejamos estos posibles errores
haciendo que nuestros programas sepan que camino tomar.

Para manejar una excpción de forma predeterminada empleamos los bloques
try-except que son básicamente los try-catch de java.

Dentro del bloque except se puedne ir especificando los bloques con
respecto a diferentes excepciones. El excepción más general que
se suele emplear es Exception.
"""


def division(a: int, b: int):
    try:
        return {
            'success': True,
            'message': 'OK',
            'result': a/b,
        }
    except TypeError as e:
        return {
            'success': False,
            'message': f'Both a & b must be numbers',
            'result': None
        }
    except ZeroDivisionError as e:
        return {
            'success': False,
            'message': f'b cannot be zero',
            'result': None,
        }


def show_example_01():
    colores = ['red', 'green', 'blue']
    try:
        print(colores[3])
    except IndexError as e:
        print(e)


def show_example_02():
    colors = ['red', 'green', 'blue']
    try:
        print(colors[3])
    except LookupError as e:
        print(e.__class__, '-', e)


def show_example_03():
    result = division(10, 0)
    print(result)


def show_example_04():
    result = division('10', '2')
    print(result)


def main():
    show_example_01()
    show_example_02()
    show_example_03()
    show_example_04()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
