"""DECORADOR wraps

Decorador utilizado comúnmente en funciones y métodos
con el objetivo de preservar metadatos de la función
original que envuelve.

Se emplea principalmente para mantener información como
el nombre de la función, documentación y firma.

Cuando decoras una función con otro decorador sin usar 
@wraps, puedes encontrarte con que la función decorada 
pierde su identidad y se convierte en la función que 
la envuelve, lo que puede afectar a la legibilidad 
del código y a su comportamiento. 

Al utilizar @wraps, la función envolvente se 
"envuelve" alrededor de la función original de 
manera que la función resultante conserva 
todas las propiedades de la función original.
"""
from functools import wraps


def showExample01():

    def myDecorator(fn):

        def wrapper(*args, **kwargs):
            print('Something is happening before the function is called...')
            result = fn(*args, **kwargs)
            print('Something is happening after the function is called...')
            return result

        return wrapper

    @myDecorator
    def sayHello():
        """Simple sayHello function."""
        return 'Hello'

    print(sayHello.__name__)
    print(sayHello.__doc__)


def showExample02():

    def myDecorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print('Something is happening before the function is called...')
            result = fn(*args, **kwargs)
            print('Something is happening after the function is called...')
            return result

        return wrapper

    @myDecorator
    def sayHello():
        """Simple sayHello function."""
        return 'Hello'

    print(sayHello.__name__)
    print(sayHello.__doc__)


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
