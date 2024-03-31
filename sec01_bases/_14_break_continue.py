"""BREAK Y CONTINUE

Se emplean para romper o saltar iteraciones dentro de los
bucles.
"""


def show_example_02():
    while True:
        print('Hello from while')
        break


def main():
    show_example_02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
