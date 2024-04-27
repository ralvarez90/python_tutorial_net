"""DECORADOR functools.lru_cache 

El decorador lru_cache (Least Recently Used cache) es una herramienta 
muy útil en Python para optimizar funciones costosas en términos de 
tiempo de ejecución al cachear los resultados de las llamadas previas. 

Esto significa que si la función se llama con los mismos argumentos, 
en lugar de volver a calcular el resultado, se devuelve el resultado 
previamente calculado desde el caché.

Es importante tener en cuenta que lru_cache es útil cuando los argumentos 
de entrada son inmutables y la función tiene el mismo resultado para 
los mismos argumentos. Si cambian los argumentos, es posible que necesites 
invalidar el caché manualmente.
"""
from functools import lru_cache


# entero a testear
N = 50


def factorial(n: int) -> int:
    return 1 if n == 0 else n * factorial(n-1)


@lru_cache()
def factorialOptimizado(n: int) -> int:
    return 1 if n == 0 else n * factorialOptimizado(n-1)


@lru_cache
def fibonacci(n: int):
    print(f'Calculating fibonacci1 of {n}')
    return 1 if n < 2 else fibonacci(n-2) + fibonacci(n-1)


def showExample01():
    print('EXAMPLE 01. Using "normal" factorial')
    print(f'factorial({N}): {factorial(N)}')
    print()


def showExample02():
    print('EXAMPLE 02. Using "optimizad" factorial')
    print(f'factorial({N}): {factorialOptimizado(N)}')
    print()


def showExample03():
    print('EXAMPLE 03. Fibonacci sequence')
    print(f'fibonacci({N})')
    fibonacci(N)


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
