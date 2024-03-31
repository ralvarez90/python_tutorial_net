"""ITERAR LISTAS CON FOR

Las listas al ser elmentos iterables se puedne recorrer
empleando la instrucción for.

Empleamos la clase enumérate para retornar un iterable
de tuplas de la forma (n, item) donde n es un índice
y el item elemento de la secuencia que recibe como 
argumento.
"""


def show_example_01():
    cities = ['New York', 'Beiging', 'Cairo', 'Mumbai', 'México ']
    for c in cities:
        print(c)


def show_example_02():
    cities = ['New York', 'Beiging', 'Cairo', 'Mumbai', 'México ']
    for item in enumerate(cities):
        print(item)


def show_example_03():
    cities = ['New York', 'Beiging', 'Cairo', 'Mumbai', 'México ']
    for item in enumerate(cities, 1):
        print(item)


def main():
    show_example_01()
    show_example_02()
    show_example_03()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
