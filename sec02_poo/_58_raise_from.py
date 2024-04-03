"""SENTENCIA RAISE-FROM

La sentencia raise nos permite lanzar una excepción en
una determina circunstancia.

Empleando junto con este la sentencia from, 

La estructura general es
raise <ExceptionType> from <cause> donde tecnicamente
es equivalente a 
ex = ExteptionType
ex.__cause__ = cause
raise ex


En Python, la palabra clave raise se utiliza para generar 
una excepción. La cláusula from se utiliza junto con raise 
para capturar y relanzar una excepción original, manteniendo 
el rastreo de la pila original. 

Esto es útil para rastrear la causa original de la excepción, 
lo que facilita la depuración y el diagnóstico de los errores.
"""

# alias
number = int | float


def show_example_01():

    def divide(a: int, b: int) -> number:
        try:
            return a/b
        except ZeroDivisionError as ex:
            raise ValueError('b must not be zero') from ex

    divide(10, 0)


def main():
    show_example_01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
