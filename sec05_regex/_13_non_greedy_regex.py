"""EXPRESIONES REGULARES NO CODICIOSAS

También se conocen como cuantificadores peresozos (lazy quantifiers) y de 
forma predeterminada, los cuantificadores funcionan en modo codicioso. 
Significa que los cuantificadores codiciosos coincidirán con sus elementos 
anteriores tanto como sea posible para volver a la mayor coincidencia 
posible.

Por otro lado, los cuantificadores no codiciosos coincidirán lo menos posible 
para devolver la coincidencia más pequeña posible. Los cuantificadores no 
codiciosos son lo opuesto a los codiciosos.

Para convertir cuantificadores codiciosos en cuantificadores no codiciosos, 
agrega un signo de interrogación adicional (?) a los cuantificadores. 
La siguiente tabla muestra los cuantificadores codiciosos y sus 
correspondientes no codiciosos:

GREEDY      LAZY        DESCRIPCIÓN
*           *?          Hace coincidir su elemento anterior cero o más veces.
+           +?          Hace coincidir su elemento anterior 1 o más veces
?           ??          Hace coincidir su elemento anterior 0 o 1 vez
{n}         {n}?        Hace coincidir su elemento anterior n veces
{n,}        {n,}?       Hace coincidir su elemento anterior al menos n veces
{n,m}       {n,m}?      Hace coindicir su elemento anteroir de n a m veces.
"""
import re


def showExample01():
    s = '<button type="submit" class="btn">Send</button>'
    pattern = r'".+?"'
    matches = re.finditer(pattern, s)
    for m in matches:
        print(m)


def showExample02():
    # todo
    raise NotImplementedError('Add more examples.')


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
