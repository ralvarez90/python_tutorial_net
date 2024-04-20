"""SECUENCIAS PERSONALIZADAS

Implementando el correspondiente protocolo, se pueden generar
secuencias personalizadas como list, tuple, etc.

Las secuencias pueden ser inmutables o mutables.

Los métodos deben ser:

1. __len__(self)
    Se encarga de devolver la longitud de la secuencia.
    
2. __getitem__(self, indice)
    Devuelve elemento en el índice especificado. Debe manejar
    slicing si tu secuencia admite el acceso mediante slices.
    
3. __contains__(self, elemento)
    Devuelve un booleano indicando si el elemento se encuentra}
    dentro de la secuencia.

"""


def fibonacci1(n: int):
    print(f'Calculating fibonacci1 of {n}')
    return 1 if n < 2 else fibonacci1(n-2) + fibonacci1(n-1)


def showExample01():
    fibonacci1(n=10)


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
