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


def main():
    connect() or print('-'*10)
    connect(username='ra90', age=33, cp=15_900) or print('-'*10)
    connect(server='localhost', user='root', password='123admin')


if __name__ == '__main__':

    # run application
    main()

    # end message
    input('\nPress any key to continue . . . ')
