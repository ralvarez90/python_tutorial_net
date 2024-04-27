"""SLICING

Técnica que permite obtener rebanadas o subsecuencias a partir
de otras. Regularmente se emplea un rango de índices indicado
de la firma i:j donde el índice i se incluye pero no el j.

Pude tener un salto como tercer valor de la forma i:j:k, donde
k será el salto, es es decir, inicia en el índice i, y el siguiente
será i+k con i+k < j.
"""
import random


def showExample01():
    numbers = [random.randint(1, 8) for _ in range(10)]
    print(f'numbers      : {numbers}')
    print(f'numbers[2:6] : {numbers[2:6]}')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
