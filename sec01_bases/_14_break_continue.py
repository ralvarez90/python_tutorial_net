"""BREAK Y CONTINUE

Se emplean para romper o saltar iteraciones dentro de los
bucles.
"""


def show_example():
    while True:
        print('Hello from while')
        break


def main():
    show_example()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . . ')
