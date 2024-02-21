"""SINGLETON

Se encarga de crear un sola instancia única. Algunos ejemplos
de singletons ya implementados en python son el None y el
booleano True.
"""


class Singleton:

    # almacena las instancias
    __instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in Singleton.__instances:
            cls.__instances[cls] = super().__new__(cls)
        return cls.__instances[cls]
