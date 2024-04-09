"""DECORADORES DE CLASES

Recordemos que las clases que implementan __call__ son objetos Callables, 
es decir se pueden invocar. Esto solo pasa cuando se implementa en su 
interior el método __call__, por lo tanto, puede hacer este método un 
decorador.
"""


def showExample01():

    # decorador factory
    def start(n: int):
        def decorate(fn):
            def wrapper(*args, **kwargs):
                print('*'*n)
                result = fn(*args, **kwargs)
                print(result)
                print('*'*n)
                return result
            return wrapper
        return decorate

    @start(5)
    def add(a: int, b: int) -> int:
        return a+b

    add(10, 20)


def showExample02():

    class Star:
        def __init__(self, n: int) -> None:
            self.n = n

    def __call__(self, fn):
        def wrapper(*args, **kwargs):
            print('*'*self.n)
            result = fn(*args, **kwargs)
            print('*'*self.n)
            return result
        return wrapper

    # uso de class decorator
    @Star(n=5)
    def add(a: int, b: int) -> int:
        return a+b

    Star(5)(add)


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue  . . .')
