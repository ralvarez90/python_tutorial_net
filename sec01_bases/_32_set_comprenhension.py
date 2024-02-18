"""SET COMPRENHENSION

Podemos generar conjuntos por expresiones, rangos y condiciones
al igual que las listas por comprensión. Pueden incluir condiciones.
"""


def exampleSetComprenhension():
    tags = {'Django', 'Flask', 'Pandas', 'Flet'}
    lowercaseTagsV1 = {tag.lower() for tag in tags}
    lowercaseTagsV2 = set(map(lambda tag: tag.lower(), tags))
    lowercaseTagsV3 = {tag.upper() for tag in tags if tag != 'Pandas'}
    print(f'lowercaseTagsV1: {lowercaseTagsV1}')
    print(f'lowercaseTagsV2: {lowercaseTagsV2}')
    print(f'lowercaseTagsV3: {lowercaseTagsV3}')


if __name__ == '__main__':

    # run examples
    exampleSetComprenhension()

    # end application
    input('\nPress any key to continue . . . ')
