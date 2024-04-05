"""OPERADOR IS, IS NOT E ==

1. Operador is
Operador binario que compara dos variables y retorna True si sus
referencias apuntan al mismo objeto. Si dos variables almacenan
referencias a diferentes objetos entonces el operador is retorna
False.

Básicamente permmite saber si dos variables apuntan al mismo objeto
(dos objetos son el mismo).

El operador is se conoce como el operador de identidad.

2. Operador ==
Por otro lado, el operador de igualdad == compara el estado de dos
objetos, aunque depende del tipo de dato que se está comparado.

3. Operador is not
Es equivalente a la negación del operador de identidad.
"""


def showExample01():
    # identidad
    a = 100
    b = 100
    print(f'a: {a}, with id: {hex(id(a))}')
    print(f'a: {b}, with id: {hex(id(b))}')
    print(f'a is b ? {a is b}')
    print(f'a == b ? {a == b}')

    # objetos con el mismo estado, pero diferente identidad
    listA = [1, 2, 3]
    listB = [1, 2, 3]
    print(f'listA: {listA}, with id: {hex(id(listA))}')
    print(f'listB: {listB}, with id: {hex(id(listB))}')
    print(f'listA is listB ? {listA is listB}')
    print(f'listA == listB ? {listA == listB}')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
