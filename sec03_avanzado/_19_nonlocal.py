"""SCOPE NONLOCAL

Recordemos que las funciones en python son ciudadanos
de primera clase, esto nos dice que pueden ser tratadas
como variables y por lo tanto podemos tener funciones
anidadas dentro de otras.

Si tengo una función B, contenida dentro de una función A,
si dentro de B tengo una variable nonnlocal x, entonces 
le estoy indicando a python que dicha variable no es local
a B, más bien es local a A. 
"""


def showExample01():
    message: str = 'Hello desde showExample01'

    def outer():
        print('Dentro de outer function...')

        def inner():
            nonlocal message
            message = message.upper()
            print('dentro de inner function..')
        inner()

    outer()
    print(f'showExample01.message: {message}')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
