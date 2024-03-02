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


def show_example_1():
    print(f'{"hello".upper()} WORLD!')
    print('{} WORLD!'.format('hello'.upper()))
    print('%s WORLD!' % ('hello'.upper()))


def show_example_2():
    fname = 'John'
    lname = 'Wick'
    fullname = F'Hello, {" ".join((fname, lname))}!'
    print(fullname)


def show_example_3():
    name = 'John Wick'
    site = 'www.johnwick.com'
    message = (
        f'Hello {name}\n'
        f"You're learning be a Killer in {site}"
    )
    print(message)


def show_example_4():
    print(f'Curly braces: {{}}')


def show_example_5():
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
    show_example_1()
    show_example_2()
    show_example_3()
    show_example_4()
    show_example_5()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . .')
