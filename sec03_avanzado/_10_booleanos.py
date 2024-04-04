"""BOOLEANOS

Extienden de los enteros, y son instancias de la
clase bool. Son inmutables y representan estados 
de verdadero y falso.

Los objetos True y False son singletons de la clase
bool.

Notas:
- Podemos emplear la clase issubclass para verificar
que en efecto la clase bool extiende de int.
"""


def runtime_type(obj: object) -> str:
    return str(type(obj))[8:-2]


def show_example_01():
    print(f'bool is subclase de int: {issubclass(bool, (int,))}')
    v = True
    print(f'{v} es un booleano ? {isinstance(v, bool)}')
    print(f'{v} es un entero   ? {isinstance(v, int)}')


def main():
    show_example_01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
