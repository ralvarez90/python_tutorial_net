"""7 FORMAS DE CONCATENAR STRINGS

Los siguientes ejemplos muestras las diversas formas que
tenemos en python para concatener strings.
"""


def showExample01():
    s = ('Esto' ' es un string concatenado1')
    print(s)


def showExample02():
    s = 'Esto' + ' es un string concatenado2'
    print(s)


def showExample03():
    s = ' '.join(['Esto', 'es un string concatenado3'])
    print(s)


def showExample04():
    s = '%s %s' % ('Esto', 'es un string concatenado4')
    print(s)


def showExample05():
    s = f'{"Esto"} {"es un string concatenado5"}'
    print(s)


def showExample06():
    s = '{} {}'.format('Esto', 'es un string concatenado6')
    print(s)


def main():
    showExample01()
    showExample02()
    showExample03()
    showExample04()
    showExample05()
    showExample06()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
