"""REGEX GREEDY

De forma predeterminada, todos los cuantificadores funcionan en 
modo codicioso. Significa que los cuantificadores intentarán 
hacer coincidir sus elementos anteriores tanto como sea posible.

De forma predeterminada, el cuantificador (+) se ejecuta en modo 
codicioso, en el que intenta hacer coincidir el elemento anterior 
(".) tanto como sea posible.

Para solucionar este problema, debe indicarle al cuantificador (+) 
que use el modo no codicioso (o perezoso), esto se hace agregando
el question mark? despues de usa run cuantificador.

Cuando el ? se emplea despes de un cuantificador, cambia el cuantificador
codicioso a no codicioso. Esto significa que la coincidencia se 
hará con la menor cantidad posible de caracteres.
"""
import re


def printSeparator(length: int = 50):
    print('-'*length)


def showExample01():
    print('EXAMPLE 01. Using greedy regex ".+"')
    s = '<button type="submit" class="btn">Send</button>'
    pattern = r'".+"'
    matches = re.finditer(pattern, s)
    for m in matches:
        print(m.group())
    printSeparator()


def showExample02():
    print('EXAMPLE 02. Using non greedy (lazy) regex ".+?"')
    s = '<button type="submit" class="btn">Send</button>'
    pattern = r'".+?"'
    matches = re.finditer(pattern, s)
    for m in matches:
        print(m.group())
    printSeparator()


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
