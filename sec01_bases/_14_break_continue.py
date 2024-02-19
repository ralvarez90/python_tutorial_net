"""BREAK Y CONTINUE

Se emplean para romper o saltar iteraciones dentro de los
bucles.
"""


def break_example():
    while True:
        print('Hello from while')
        break


if __name__ == '__main__':

    # ejemplod de uso de break
    break_example()

    # end message
    input('\nPress any key to continue . . . ')
