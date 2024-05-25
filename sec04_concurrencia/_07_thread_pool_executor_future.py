"""THREAD POOL EXECUTOR EXAMPLE

1. Future
Es un objeto que representa un eventual resultado de una operación
asíncrona, es equivalente a las promesas en javascript. La clase
Future tiene dos métodos útiles:

- result(), que regresea el resultado de la operación asíncrona
- exception(), que regresa una excepción de una operación asíncrona en
caso de que ocurra una excepción.

Dentro un context manager de un ThreadPool, el método submit 
recibe la función a ejecutar de forma asíncrona seguido
de sus argumentos en caso de que reciba.
"""
from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor


def showExample01():

    # some function task
    def task(id: int) -> str:
        print('Starting the task %d...' % (id))
        sleep(1)
        return 'Done with task %d' % (id)

    # create thread pool context manager
    with ThreadPoolExecutor(max_workers=16) as executor:
        f1 = executor.submit(task, 1)
        f2 = executor.submit(task, 2)

        # get results
        print(f1.result())
        print(f2.result())

    print('End to showExample01...')


def showExample02():

    # some function task
    def task(id: int) -> str:
        print('Starting the task %d. . . ' % (id))
        sleep(1)
        return 'Done with task %d' % (id)

    with ThreadPoolExecutor(max_workers=16) as executor:
        # list of futures
        futures = [executor.submit(task, i) for i in range(1, 101)]
        [f.result for f in futures]

    print('End to showExample02. . . ')


def main():

    # init time
    ti = perf_counter()
    showExample01()
    t2 = perf_counter()
    print('Time example01: %.2f seconds...' % (t2 - ti))
    print()

    # init time
    ti = perf_counter()
    showExample02()
    t2 = perf_counter()
    print('Time example02: %.2f seconds...' % (t2 - ti))
    print()


# run application
if __name__ == '__main__':
    main()
