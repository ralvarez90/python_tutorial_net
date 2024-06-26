"""SET COMPRENHENSION

Podemos generar conjuntos por expresiones, rangos y condiciones
al igual que las listas por comprensión. Pueden incluir condiciones.
"""


def showExample01():
    tags = {'Django', 'Flask', 'Pandas', 'Flet'}
    lowercaseTags1 = {tag.lower() for tag in tags}
    lowercaseTags2 = set(map(lambda tag: tag.lower(), tags))
    lowercaseTags3 = {tag.upper() for tag in tags if tag != 'Pandas'}
    print(f'lowercaseTags1: {lowercaseTags1}')
    print(f'lowercaseTags2: {lowercaseTags2}')
    print(f'lowercaseTags3: {lowercaseTags3}')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
