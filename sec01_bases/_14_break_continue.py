"""BREAK Y CONTINUE

Se emplean para romper o saltar iteraciones dentro de los
bucles.
"""


def showExample01():
    while True:
        print('Hello from while')
        break


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
