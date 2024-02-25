"""7 FORMAS DE CONCATENAR STRINGS

"""


def concatenacion1():
    s = 'Esto' ' es un string concatenado1'
    print(s)


def concatenacion2():
    s = 'Esto' + ' es un string concatenado2'
    print(s)


def concatenacion3():
    s = ' '.join(['Esto', 'es un string concatenado3'])
    print(s)


def concatenacion4():
    s = '%s %s' % ('Esto', 'es un string concatenado4')
    print(s)


def concatenacion5():
    s = f'{"Esto"} {"es un string concatenado5"}'
    print(s)


def concatenacion6():
    s = '{} {}'.format('Esto', 'es un string concatenado6')
    print(s)


def main():
    concatenacion1()
    concatenacion2()
    concatenacion3()
    concatenacion4()
    concatenacion5()
    concatenacion6()
    return


if __name__ == '__main__':
    main() or input('\nPress any key to continue . . .')
