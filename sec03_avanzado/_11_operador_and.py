"""OPERADOR AND

Operador lógico binario que retorna true cuando el valor
de ambos operadores es True, en caso contrario regresa
False.

La característica clave del operador and es que provoca 
un cortocircuito. Significa que si el primer operando 
es Falso, el operador y no evaluará el segundo operando. 

La razón es que ya tiene una conclusión sobre el 
resultado, que es falsa.
"""


def avg(*numbers):
    total = sum(numbers)
    n = len(numbers)
    return n and total/n


def showExample01():
    a: int = int(input('a int: '))
    b: int = int(input('b int: '))
    c = b and a/b
    result = None if b is 0 else c
    if result:
        print(f'a/b -> {a}/{b} = {result}')


def showExample02():
    print(avg())
    print(avg(1, 2, 3))
    print(avg(0, 0, 0))
    print(avg(0, 0, 0, 1))


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
