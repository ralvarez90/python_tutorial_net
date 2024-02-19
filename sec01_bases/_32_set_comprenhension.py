"""SET COMPRENHENSION

Podemos generar conjuntos por expresiones, rangos y condiciones
al igual que las listas por comprensión. Pueden incluir condiciones.
"""


def example_comprenhension_sets():
    tags = {'Django', 'Flask', 'Pandas', 'Flet'}
    lowercaseTagsV1 = {tag.lower() for tag in tags}
    lowercaseTagsV2 = set(map(lambda tag: tag.lower(), tags))
    lowercaseTagsV3 = {tag.upper() for tag in tags if tag != 'Pandas'}
    print(f'lowercaseTagsV1: {lowercaseTagsV1}')
    print(f'lowercaseTagsV2: {lowercaseTagsV2}')
    print(f'lowercaseTagsV3: {lowercaseTagsV3}')


def main():
    # run single example
    example_comprenhension_sets()


if __name__ == '__main__':

    # run application
    main()

    # end message
    input('\nPress any key to continue . . . ')
