"""CUANTIFICADORES

En las expresiones regulares, los cuantificadores coinciden con 
los caracteres o conjuntos de caracteres anteriores varias veces. 

La siguiente tabla muestra todos los cuantificadores y sus 
significados:

*
    Hace coincidir su elemento anterior cero o más veces.

+
    Hace coincidir su elemento anterior 1 o más veces
    
?
    Hace coincidir su elemento anterior 0 o 1 vez.
    
{n}
    Hace coincidir su elemento anterior exactamente n veces.
    
{n,}
    Hace coincidir su elemento anterior al menos n veces

{n, m}
    Hace coincidir su elemento anterior de n a m veces.
    
----------------------------------------------------------

\w      matchea cualquier caracter simple
\w*     matchea zero o más caracteres
\d      matchea un dígito
\d+     matchea uno o más dígitos 

"""
import re


def printSeparator(length: int = 50):
    print('-'*length)


def showExample01():
    print('EXAMPLE 01. Match zero o more times (*)')

    # string content
    s = """\"CPython, IronPython, and Jython are major Python's
    \rimplementation\""""
    print(s)

    # regex, matchea cualquier
    pattern = re.compile(r'\w*Python')
    for m in pattern.finditer(s):
        print(m.group())

    printSeparator()


def showExample02():
    print('EXAMPLE 02. Match one or more times (+)')

    # string content
    s = 'Python 3.10 was released in 2021'
    print(f'"{s}"')
    matches = re.finditer(r'\d+', s)
    for m in matches:
        print(m.group())
    printSeparator()


def showExample03():
    print('EXAMPLE 03. Match zero or one time (?)')

    # string content
    s = 'What color / colour do you like?'
    print(s)

    # matchea colour y color
    matches = re.finditer(r'colou?r', s)
    for m in matches:
        print(m.group())
    printSeparator()


def showExample04():
    print('EXAMPLE 04. Match exactly n times: {n}')

    # string content
    s = 'It was 11:05 AM'
    print(s)

    matches = re.finditer(r'\d{2}:\d{2}', s)
    for m in matches:
        print(m.group())
    printSeparator()


def showExample05():
    print('EXAMPLE 05. Match at least n times: {n,}')

    # string content
    s = '5-5-2021 or 05-05-2021 or 5/5/2021 or 05/05/2021'
    matches = re.finditer(r'\d{1,}-\d{1,}-\d{4}', s)
    for m in matches:
        print(m.group())
    printSeparator()


def showExample06():
    print('EXAMPLE 06. Match from n and m times: {n, m}')

    # string content
    s = '5-5-2021 or 05-05-2021 or 5/5/2021 or 05/05/2021'
    matches = re.finditer(r'\d{1,2}-\d{1,2}-\d{4}', s)
    for m in matches:
        print(m.group())
    printSeparator()


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
