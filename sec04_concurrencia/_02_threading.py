"""MÓDULO THREADING

Por default los programas en python son single-thread, lo que
queire decir que todo se ejecuta de forma secuencial en un mismo
hilo.

Empleamos la clase Thread del módulo threading para ejecutar programas
multihilo.

Una instancia de Thread recibe una función objetivo, y una tupla de
argumentos.

Una vez creada una instancia de Thread, se ejecuta start y se agrega
mediante el método join al main thread, esto hace que la tarea asignada
al thread se complete.

Los procesos y los threads significativamente se emplean para diversas
cosas. Los threas se utilizan para operaciones de entrada/salida de datos
mientras que los procesos para tareas con requerimientos significativos.
"""
from time import perf_counter, sleep
from threading import Thread


def showExample01():

    def task():
        print('Starting a task...')
        sleep(1)
        print('done...')

    ti = perf_counter()
    task()
    task()
    tf = perf_counter()
    print(f'showExample01 se ejecuta en {tf-ti} segundos')


def showExample02():

    def task():
        print('Starting task...')
        sleep(1)
        print(f'done...')

    # tiempo inicial
    ti = perf_counter()

    # se crean hilos, se ejecutan y se agregan al main thread
    threadsToExec = [Thread(target=task) for _ in range(10)]
    [t.start() for t in threadsToExec]
    [t.join() for t in threadsToExec]

    # contador final
    tf = perf_counter()
    print(f"showExample02 se ejecuta en {tf-ti} segundos")


def showExample03():

    def task(id: int):
        print(f'Starting task {id}...')
        sleep(1)
        print(f'The task {id} completed...')

    # contador inicial
    ti = perf_counter()

    # se crean hilos, se ejecuta y se agregan al main thread
    threadsToExec = [Thread(target=task, args=(i,)) for i in range(1, 1001)]
    [t.start() for t in threadsToExec]
    [t.join() for t in threadsToExec]

    # contador final
    tf = perf_counter()
    print(f'showExample03 se ejecuta en {tf-ti} segundos')


def showExample04():
    
    def replace(filename, substr, newSubstr):
        print(f'Processing the file: {filename}')


def main():
    # showExample01()
    # showExample02()
    showExample03()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
