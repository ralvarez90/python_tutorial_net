"""7 FORMAS DE CONCATENAR STRINGS

Los siguientes ejemplos muestras las diversas formas que
tenemos en python para concatener strings.
"""


def show_example_1():
    s = 'Esto' ' es un string concatenado1'
    print(s)


def show_example_2():
    s = 'Esto' + ' es un string concatenado2'
    print(s)


def show_example_3():
    s = ' '.join(['Esto', 'es un string concatenado3'])
    print(s)


def show_example_4():
    s = '%s %s' % ('Esto', 'es un string concatenado4')
    print(s)


def show_example_5():
    s = f'{"Esto"} {"es un string concatenado5"}'
    print(s)


def show_example_6():
    s = '{} {}'.format('Esto', 'es un string concatenado6')
    print(s)


def main():
    show_example_1()
    show_example_2()
    show_example_3()
    show_example_4()
    show_example_5()
    show_example_6()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . .')
