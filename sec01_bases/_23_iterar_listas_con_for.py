"""ITERAR LISTAS CON FOR

Las listas al ser elmentos iterables se puedne recorrer
empleando la instrucción for.

Empleamos la clase enumerate para retornar un iterable
de tuplas de la forma (n, item) donde n es un índice
y el item elemento de la secuencia que recibe como 
argumento.
"""


def show_example_1():
    cities = ['New York', 'Beiging', 'Cairo', 'Mumbai', 'México ']
    for c in cities:
        print(c)


def show_example_2():
    cities = ['New York', 'Beiging', 'Cairo', 'Mumbai', 'México ']
    for item in enumerate(cities):
        print(item)


def show_example_3():
    cities = ['New York', 'Beiging', 'Cairo', 'Mumbai', 'México ']
    for item in enumerate(cities, 1):
        print(item)


def main():
    show_example_1()
    show_example_2()
    show_example_3()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . . ')
