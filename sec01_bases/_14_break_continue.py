"""BREAK Y CONTINUE

Se emplean para romper o saltar iteraciones dentro de los
bucles.
"""


def breakExample():
    while True:
        print('Hello from while')
        break


if __name__ == '__main__':

    # break
    breakExample()

    # end application
    input('\nPress any key to continue . . . ')
