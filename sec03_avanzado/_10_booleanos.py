"""BOOLEANOS

Extienden de los enteros, y son instancias de la
clase bool. Son inmutables y representan estados 
de verdadero y falso.

Los objetos True y False son singletons de la clase
bool.

Las instancias de bool son singletons, esto permite
poder usar el operador is e == para compararlos.

Otra característica importante de python es que
todos los objetos pueden evaluarse como booleanos.
Recordemos que el método __bool__ es el que se encarga
de definir este comportamiento.

Notas:
- Podemos emplear la clase issubclass para verificar
que en efecto la clase bool extiende de int.
"""


def runtimeType(obj: object) -> str:
    return str(type(obj))[8:-2]


def showExample01():
    print(f'bool is subclase de int: {issubclass(bool, (int,))}')
    v = True
    print(f'{v} es un booleano ? {isinstance(v, bool)}')
    print(f'{v} es un entero   ? {isinstance(v, int)}')


def showExample02():
    print(f'True is True = {True is True}')
    print(f'True is False = {True is False}')
    print(f'True == True = {True == True}')
    print(f'True == False = {True == False}')


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
