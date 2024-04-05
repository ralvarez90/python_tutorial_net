"""OPERADOR OR

Operador booleano que se evalúa como True en caso de que
alguno de los operandos (o expresiones) se evalúa como True.

Al igual que or es un operador en corto circuito. Esto permite
poder usarlo para asignar valores default, en caso de que un
objeto sea nulo o sea evalúe como nulo.
"""


def showExample01():
    print("Hola mundo" or None)


def showExample02():
    favoriteLang = input('Input your favorite language: ') or 'Python'
    print(f'Your favorite language is {favoriteLang.title()}')


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
