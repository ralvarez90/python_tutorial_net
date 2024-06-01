"""GRUPOS DE CAPTURA

\w+
    El \w junto con el cuantificador +, matchea cualquier string de longitud
    1 o mayor.

/
    Matchea el carater /

\d+
    Matchea cualquier dígito de longitud 1 o mayor.
    
El método group le permite acceder a los subgrupos matcheados dentrel de la
regex, donde si es cero retorna el matcheao completo.
"""
import re


def printSeparator(length: int = 50):
    print('-'*length)


def showExample01():
    print('EXAMPLE 01. Using r"\w+/\d+" regex')
    s = 'news/100'
    pattern = r'\w+/\d+'
    matches = re.finditer(pattern, s)
    for m in matches:
        print(m.group())
    printSeparator()


def showExample02():
    print('EXAMPLE 02. Using r"\w+/(\d+)" regex')
    s = 'news/100'
    pattern = r'\w+/(\d+)'
    matches = re.finditer(pattern, s)
    for m in matches:
        print(m.group())
    printSeparator()


def showExample03():
    print('EXAMPLE 03. Using r"\w+/(\d+)" regex and match.group(index)')
    s = 'news/100'
    pattern = r'\w+/(\d+)'
    matches = re.finditer(pattern, s)
    for match in matches:
        for i in range(0, match.lastindex + 1):
            print(match.group(i))
    printSeparator()


def showExample04():
    print('EXAMPLE 04. Using match.group with index again')
    s = 'Hoy es 01-06-2024'
    pattern = r'(\d{2})-(\d{2})-(\d{4})'
    m = re.search(pattern, s)
    if m:
        for i in range(0, m.lastindex+1):
            print(m.group(i))
    printSeparator()


def showExample05():
    # todo: crear ejemplo con groupdict
    pass


def main():
    showExample01()
    showExample02()
    showExample03()
    showExample04()
    showExample05()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
