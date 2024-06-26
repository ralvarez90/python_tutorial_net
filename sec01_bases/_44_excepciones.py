"""EXCEPCIONES

En python existen dos tipos de errores. De Sintaxis y excepciones. Todo
código bien escrito en python puede causar errores al momento de 
ejecutarse. En python los errores en tiempo de ejecución se denominan
excepciones.

1. try-except
Python cuenta con mecanismos para el manejo de errores. Los bloques 
try y except nos ayudan a manejarlos.

Dentro del bloque except se puede atrapart 1 o más tipos de excepciones,
por lo que pidemos ir del más particular al más general o simplemente
usar el general Exception.

La forma en el que se implementa el try-raise es
try:
    posibles
    errores
except TipoException as err:
    manejo de excepcion con el
    alias del objeto err
except Exception:
    instrucciones...
finally
    Se ejecuta siempre.
    
Si se agrega el bloque finally al final este siempre se ejecuta existea
o no excepción.

Otra estructura es
try:
    codigo
    ...
except:
    codigo
    ...
else:
    Se ejecuta en el momento que no ocurre una excepción.
    
Podemo combinar try-except-else-finally de forma que el
else se ejecuta solo si no hay excepciones y el finally siempre.
"""


def calcularIMC(height: float, weight: float):
    return weight/height**2


def showExample01():
    try:
        # ingreso datos
        print('Enter the net sales for:')
        previo = float(input('- Priod period:'))
        current = float(input('- Current period:'))

        # calculo  diferencia
        change = (current - previo)*100 / previo

        if change > 0:
            results = 'Sales increase: %.2f' % (abs(change))
    except Exception as err:
        print(err)
    finally:
        print('Esto SIEMPRE se ejecuta...')


def showExample02():
    try:
        height = float(input('Enter your height: '))
        weight = float(input('Enter your weight: '))
    except ValueError as error:
        print(error)
    else:
        bmi = round(calcularIMC(height, weight))
        print('BMI: %.2f' % (bmi))


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
