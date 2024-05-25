"""FULLMATCH FUNCTION

Retorna un objeto Match si toda la cadena coincide con el patrón,
de otra forma retorna un None.

Notas:
- El patrón \d{4} matchea todos los números de 4 dígitos.
"""
import re


def showExample01():

    s1 = '2031'
    s2 = 'Python 3.10 released in 2021'
    pattern = r'\d{4}'
    print(re.fullmatch(pattern, s1))
    print(re.fullmatch(pattern, s2))


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
