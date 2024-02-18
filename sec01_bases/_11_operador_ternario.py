"""OPERADOR TERNARIO

En python no existe el operador ternario como en java u otros
lenguajes. Se puede simplificar el if-else de dos formas:

1. expresions_si_true if condicion else expresion_si_false
2 (expresion_si_false, expresion_si_true)[condicion]

Son las dos alternativas que brinda python al operador ternario.
"""


def mostrarTernarioVersion1():
    age = int(input('age: '))
    message = 'Welcome' if age >= 18 else 'Bye!'
    print(f'message_v1: {message}')


def mostrarTernarioVersion2():
    age = int(input('age: '))
    message = ('Bye!', 'Welcome')[age >= 18]
    print(f'message_v2: {message}')


if __name__ == '__main__':

    # v1
    mostrarTernarioVersion1()

    # v2
    mostrarTernarioVersion2()

    # end application
    input('\nPress any key to continue . . . ')
