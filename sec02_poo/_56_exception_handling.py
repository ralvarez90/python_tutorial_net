"""MANEJO DE EXCEPTIONS

Para el manejod de posibles excepciones disponemos de los siguientes
bloques:
- try
- except
- else
- finally

1. try
Es el bloque que contiene  código que puede lanzar potencialmente excepciones. Un bloque try puede
tener cero o más cláusulas except asociadas.

De forma general el bloque se usa
try:
    ...
except ExceptionType1 as e:
    ...
except ExceptionTyoe2 as e:
    ...
except Exception as e:
    ...
else:
    ...
finally:
    ...
    
donde else se ejecuta si y solo si el bloque trye se ejecuta correctamente sin excepciones,
finally se ejecuta siempre, ocurra o no excepción.
"""


number = int | float


def divide(a: int, b: int) -> number | None:
    try:
        return a/b
    except ZeroDivisionError as e:
        return None


def show_example_01():
    result = divide(10, 0)
    if result is not None:
        print(f'Result: {result}')
    else:
        print(f'Invalid inputs')


def main():
    show_example_01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
