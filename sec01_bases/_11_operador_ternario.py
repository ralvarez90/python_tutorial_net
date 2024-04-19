"""OPERADOR TERNARIO

En python no existe el operador ternario como en java u otros
lenguajes. Se puede simplificar el if-else de dos formas:

1. expresions_si_true if condicion else expresion_si_false
2. (expresion_si_false, expresion_si_true)[condicion]

Son las dos alternativas que brinda python al operador ternario.

Nota:
- En el caso del segundo 'operador ternario', recordemos que los
booleanos extienden de los enteros por lo cual pueden ser
usados como índices.
"""


def showExample01():
    age = int(input('age: '))
    message = 'Welcome' if age >= 18 else 'Bye!'
    print(f'message_v1: {message}')


def showExample02():
    age = int(input('age: '))
    message = ('Bye!', 'Welcome')[age >= 18]
    print(f'message_v2: {message}')


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
