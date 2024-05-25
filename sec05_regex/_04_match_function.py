"""MÉTODO re.match

Retorna un Match object al igual que re.search. Este retorna un
Match si encuentra una coincidencia con el patrón al inicio del
string.

Notas:
- El patrón r'\w' representa cualquier caracter alfanumérico
o guión bajo. Recordar que coincide con un solo caracter.
"""
import re


def showExample01():
    print('Example 01. Using re.match method.')

    # strings messages
    contents = [
        'Python',                                               # si
        'CPython is an implementation of Python written in C',  # no
        'Jython is a Java implementation of Python',            # si
        'IronPython is Python on .NET framework',               # no
    ]

    # regex pattern
    pattern = r'\wython'

    allMatches = []
    for msg in contents:
        result = re.match(pattern, msg)
        print(result)


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
