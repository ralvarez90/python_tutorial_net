"""CONVERSIÓN DE TIPOS

Como sabemos python no es un lenguaje con sistema de tipos
fijo, es decir, los objetos pueden ir cambiando de tipos
durante la ejecución del programa.

Algunos constructores permiten recibir objetos para poder
hacer conversiones entre tipos.

1. Función input
Retorna un string, que dependiendo de su contenido se puede
transformar en entero, flotante u otros tipos de de datos.

Podemos emplear las clases siguientes para realizar conversiones
entre diversos tipos de datos.
- int
- float
- bool
- str

2. Clase type
Retorna un objeto que permite obtener información acerca del tipo
de objeto que recibe en su constructor.

Notas:
- En python todo es un objeto y las clases no son la excepción. Las
clases extienend de type.
"""


def runtime_type(obj: object) -> str:
    """Retorna un string del tipo de dato
    del argumento.

    >>> runtime_type('Hello')
    'str'

    >>> runtime_type(1)
    'int'
    """
    return str(type(obj))[8:-2]


if __name__ == '__main__':

    # algunas instancias
    instancias = (1, 1.0, 0j, True, 'hola')

    # show types
    for obj in instancias:
        print('{:<5} has a type {}'.format(obj, runtime_type(obj)))

    # end application
    input('\nPress any key to continue . . .')
