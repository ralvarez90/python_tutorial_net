"""GESTORES DE CONTEXTO

Un gestor de contexto (context manager) es un onjeto que define
en tiempo de ejecución se emplea junto con with para crear
un contexto.

Estos funciones en base el context manager protocol definido
por los siguientes métodos:

__enter__
	Establece el contexto y opcionalmente retorna un objeto

__exit__
	Limpia de forma segura el objeto en cuestión.
"""
from time import perf_counter


def showExample01():

    class File:
        def __init__(self, filename, mode) -> None:
            self.filename = filename
            self.mode = mode

        def __enter__(self):
            print(f'Opening the file: "{self.filename}".')
            self.__file = open(self.filename, self.mode)
            return self.__file

        def __exit__(self, exc_type, exc_value, exc_traceback):
            print(f'Closing tje file: {self.filename}')
            if not self.__file.closed:
                self.__file.close()
            return False


def showExample02():

    class Timer:
        def __init__(self) -> None:
            self.elapsed = 0

        def __enter__(self):
            self.start = perf_counter()
            return self

        def __exit__(self, exc_type, exc_value, exc_traceback):
            self.stop = perf_counter()
            self.elapsed = self.stop - self.start
            return False

    def fibonacci(n: int):
        f1 = 1
        f2 = 1
        for i in range(n-1):
            f1, f2 = f2, f1 + f2
        return f1

    with Timer() as timer:
        for _ in range(1, 1_000_000):
            fibonacci(1000)

        print(timer.elapsed)


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
