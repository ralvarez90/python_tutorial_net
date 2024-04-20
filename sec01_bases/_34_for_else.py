"""FOR ELSE

El ciclo for permite establecer un bloque else que se
ejecuta cuando termina de iterar sobre los elementos
correspondientes.

Si el iterable en cuestión no se termina de iterar
(ocurre por ejemplo break), entonces el bloque else
NO se ejecuta.
"""


def showExample01():
    people = [
        {'name': 'John Doe', 'age': 25},
        {'name': 'Mary Jane', 'age': 22},
        {'name': 'Peter Parker', 'age': 34},
    ]
    print(f'people: {people}')
    name = input('name: ')
    found = False
    for person in people:
        if person['name'] == name:
            found = True
            print(person)
            break
    else:
        print(f'{name} not found!')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue. . . ')
