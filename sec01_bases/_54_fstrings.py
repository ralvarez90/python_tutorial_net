"""STRINGS CON FORMATO

1. fstrings
Son string que inician con una f y permiten interpolar
datos dentro de estas empleando los corchetes. Podemos
evaluar expresiones dentro de los corchetes como se
muestra en la función fstringExample.

2. Los strings tienen un método llamado format que 
de igual forma permiten interpolar valores.

Si quiere agregar llaves y usar string format se agregan
dobles.

3. Los valors numéricos pueden ser mostrados con cierto
formatos. 

{number:e}
Muestra el número con notación exponencial.
"""


def showExample01():
    print(f'{"hello".upper()} WORLD!')
    print('{} WORLD!'.format('hello'.upper()))
    print('%s WORLD!' % ('hello'.upper()))


def showExample02():
    fname = 'John'
    lname = 'Wick'
    fullname = f'Hello, {" ".join((fname, lname))}!'
    print(fullname)


def showExample03():
    name = 'John Wick'
    site = 'www.johnwick.com'
    message = (
        f'Hello {name}\n'
        f"You're learning be a Killer in"
        f' {site}'
    )
    print(message)


def showExample04():
    print(f'Curly braces: {{}}')


def showExample05():
    number = 0.01
    print(f'{number:e}')
    print(f'{number:E}')
    print(f'{number:.2f}')
    print(f'{number:010}')

    number = 1_000_000_000
    print(f'${number:,.2f}')

    number = 0.75
    print(f'{number:.1%}')


def main():
    showExample01()
    showExample02()
    showExample03()
    showExample04()
    showExample05()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
