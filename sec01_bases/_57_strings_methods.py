"""MÉTODOS DE STRINGS

Dentro de los métodos de los strings tenemos los siguientes:

join
Retorna un string que concatena los strings dentro deun iterable.

concat
Retorna un string resultado de la concatenación de dos o más strings.

split
Retorna una lista de substrings usando el argumento como separador.

index
Retorna el índice de un substring o lanza un ValueError si no exite
el substring dentro.

find
Retorna el índice de la primer ocurrencia de un substring. Retorna -1
si no existe.

startswith, endswith
Retorna booleanos indicando si un string inicia o finaliza con determinado
substring.
"""
# TODO - Agregar descripción y ejemplos de métodos de los strings


def show_example_1():
    elements = ('red', 'green', 'blue')
    rgb = ', '.join(elements)
    print(f'rgb: {rgb}')


def show_example_2():
    s = 'Python String Split'
    print(s.split())
    print(s.split(maxsplit=1))


def main():
    show_example_1()
    show_example_2()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . .')
