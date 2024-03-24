"""DICCIONARIOS

Son iterables de pares clave-valor. Los keys se emplean como
llaves únicas. Un diccionario vacía se declara emplando {}
o la clase dict.

Son objetos indexados por su key, usamos la notación de corchetes
para acceder a cada valor de un diccionario. Se puede emplear el
método get para este fin otorgando un default a retornar en caso
de que el key no exista en el diccionario.

Agregamos elementos de la forma
diccionario[key] = valor

y eliminamos elementos empleando del diccionario[key]. Podemos iterar
meidante un for a traves de las keys, values y tuplas (key, value)
de un diccionario.

Los diccionarios tiene un serie de métodos útiles para manejarlos.
Esta es una de las estructuras de datos más importantes.
"""


def runtimeType(item: object) -> str:
    return str(type(item))[8:-2]


def showExample01():
    persona = {
        'firstName': 'Rodrigo',
        'lastName': 'Alvarez',
        'age': 33,
        'activo': True,
    }

    print(f'Persona: {persona}')
    print(runtimeType(persona))

    # iteración de keys
    for k in persona:
        print(f'persona[{k}] -> {persona[k]}')

    print(persona.get('firstName', ''))
    print(persona.get('nombre', 'sin-nombre'))


def showExample02():
    persona = {
        'firstName': 'rodrigo',
        'lastName': 'alvarez',
        'age': 33,
        'favoriteColors': ['red', 'blue'],
    }

    del persona['age']
    print(f'persona: {persona}')


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
