"""7 FORMAS DE CONCATENAR STRINGS

Los siguientes ejemplos muestras las diversas formas que
tenemos en python para concatener strings.
"""


def show_example_01():
    s = 'Esto' ' es un string concatenado1'
    print(s)


def show_example_02():
    s = 'Esto' + ' es un string concatenado2'
    print(s)


def show_example_03():
    s = ' '.join(['Esto', 'es un string concatenado3'])
    print(s)


def show_example_04():
    s = '%s %s' % ('Esto', 'es un string concatenado4')
    print(s)


def show_example_05():
    s = f'{"Esto"} {"es un string concatenado5"}'
    print(s)


def show_example_06():
    s = '{} {}'.format('Esto', 'es un string concatenado6')
    print(s)


def main():
    show_example_01()
    show_example_02()
    show_example_03()
    show_example_04()
    show_example_05()
    show_example_06()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
