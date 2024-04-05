"""FUNCIÓN ROUND

Recibe un número y retorna el valor redondeado al más cercano de 10^-ndigits. donde
n es su segundo argumento.

Utilice la función round(number, ndigits) para redondear un número a la precisión 
de ndigits después del punto decimal.

# todo - hacer ejemplo con 3 argumentos
# todo - hacer ejemplo con función math.copysign
"""


def showExample01():
    someNumber: float = 1.9876543210
    for i in range(10):
        print(f'round({someNumber}, {i}) -> {round(someNumber, i)}')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue. . .')
