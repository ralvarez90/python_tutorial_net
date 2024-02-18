"""PARÁMETRO KWARGS

Podemo recibir en funciones pares de argumentos variables de la forma
name=valor, para emplearse dentro como un diccionario. Se colocan
**kwargs por coleccion y estos se conocen como argumentos key.

Si tenemos un diccionario, podemos destructurar sus datos para pasarse
como argumentos a funciones empleando un dobke asterisco.

Se puede usar un *args y **kwargs como paraámetros en una misma función.
"""
from pprint import pprint


def runtimeType(obj: object) -> str:
    return str(type(obj))[8:-2]


def connect(**kwargs):
    print(runtimeType(kwargs))
    pprint(kwargs)


if __name__ == '__main__':

    # run examples
    connect()
    connect(name='Rodrigo', age=33, cp=15900)
    connect(server='localhost', user='root', password='Les900310@123')

    # end application
    input('\nPress any key to continue . . . ')
