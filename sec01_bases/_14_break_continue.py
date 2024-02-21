"""BREAK Y CONTINUE

Se emplean para romper o saltar iteraciones dentro de los
bucles.
"""


def breakExample():
    while True:
        print('Hello from while')
        break


def main():
    breakExample()


if __name__ == '__main__':

    # run application
    main()

    # end message
    input('\nPress any key to continue . . . ')
