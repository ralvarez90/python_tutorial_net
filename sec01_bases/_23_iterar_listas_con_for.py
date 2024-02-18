"""ITERAR LISTAS CON FOR

Las listas al ser elmentos iterables se puedne recorrer
empleando la instrucción for.

Empleamos la clase enumerate para retornar un iterable
de tuplas de la forma (n, item) donde n es un índice
y el item elemento de la secuencia que recibe como 
argumento.
"""


def iterateWithForExample():
    cities = ['New York', 'Beiging', 'Cairo', 'Mumbai', 'México ']
    for c in cities:
        print(c)


def enumerateExample1():
    cities = ['New York', 'Beiging', 'Cairo', 'Mumbai', 'México ']
    for item in enumerate(cities):
        print(item)


def enumerateExample2():
    cities = ['New York', 'Beiging', 'Cairo', 'Mumbai', 'México ']
    for item in enumerate(cities, 1):
        print(item)


if __name__ == '__main__':

    # for
    iterateWithForExample()

    # enumerate
    enumerateExample1()

    # enumerate
    enumerateExample2()

    # end application
    input('\nPress any key to continue . . . ')
