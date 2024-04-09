"""DECORADORES CON ARGUMENTOS

Los decoradores son funciones, por lo tanto pueden recibir
argumentos.

Notas:
- El decorador @wraps del módulo functools conserva los metadatos
de 
"""
from functools import wraps


def showExample01():

    def repeat(times: int):
        """Call a function a number of times."""

        def decorate(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                for _ in range(times):
                    result = fn(*args, *kwargs)
                return result
            return wrapper
        return decorate

    @repeat(10)
    def say(message: str):
        print(message)

    say("Hello World!")


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
