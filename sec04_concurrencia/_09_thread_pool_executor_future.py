"""THREAD POOL EXECUTOR EXAMPLE

1. Future
Es un objeto que representa un eventual resultado de una operación
asíncrona, es equivalente a las promesas en javascript. La clase
Future tiene dos métodos útiles:
- result(), que regresea el resultado de la operación asíncrona
- exception(), que regresa una excepción de una operación asíncrona en
caso de que ocurra una excepción.
"""
from time import sleep, perf_counter


def showExample01():

    def task(id: int):
        print('Starting the task %d...' % (id))
        sleep(1)
        return 'Done with task %d' % (id)


def main():

    # init time
    ti = perf_counter()
    print()


# run application
if __name__ == '__main__':
    main()
