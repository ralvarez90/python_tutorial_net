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
from functools import lru_cache


class Fibonacci:
    def __init__(self, n: int) -> None:
        self.n = n

    @staticmethod
    @lru_cache(maxsize=2**16)
    def fib(n: int) -> int:
        return 1 if n < 2 else Fibonacci.fib(n-2) + Fibonacci.fib(n-1)

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0 or index > self.n - 1:
                raise IndexError
            return Fibonacci.fib(index)
        else:
            indices = index.indices(self.n)
            return [Fibonacci.fib(k) for k in range(*indices)]


def showExample01():
    print('EXAMPLE 01. Accessing Fibonacci sequence using []:')
    fibonacci = Fibonacci(2**8)
    # using []
    for i in range(1, 11):
        print(fibonacci[i])


def showExample02():
    print('EXAMPLE 02. Accessing Fibonacci sequence using for loop:')
    fibonacci = Fibonacci(2**8)
    # using as a loop
    for item in fibonacci:
        print(item)


def showExample03():
    print('EXAMPLE 03. Using an slice in custom sequence')
    fibonacci = Fibonacci(2**8)
    print(f'fibonacci[1:3] -> {fibonacci[1:3]}')


def main():
    showExample01()
    showExample02()
    showExample03()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
