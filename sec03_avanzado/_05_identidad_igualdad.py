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


def show_example_01():
    # identidad
    a = 100
    b = 100
    print(f'a: {a}, with id: {hex(id(a))}')
    print(f'a: {b}, with id: {hex(id(b))}')
    print(f'a is b ? {a is b}')
    print(f'a == b ? {a == b}')

    # separador
    print('-'*50)

    # objetos con el mismo estado, pero diferente identidad
    list_a = [1, 2, 3]
    list_b = [1, 2, 3]
    print(f'list_a: {list_a}, with id: {hex(id(list_a))}')
    print(f'list_b: {list_b}, with id: {hex(id(list_b))}')
    print(f'list_a is list_b ? {list_a is list_b}')
    print(f'list_a == list_b ? {list_a == list_b}')


def main():
    show_example_01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
