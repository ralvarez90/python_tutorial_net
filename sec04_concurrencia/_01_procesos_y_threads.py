"""PROCESOS Y THREADS

Por definición, un proceso es una instancia de un programa que se ejecuta en 
una computadora. Y un hilo (thread) es una unidad de ejecución dentro de un
proceso.

Un programa es como una clase, mientras que los procesos son 
como objetos de la clase.
"""
from time import sleep, perf_counter
from threading import Thread


def task():
    print(f'starting task...')
    sleep(1)
    print(f'done')


if __name__ == '__main__':

    start = perf_counter()
    task()
    task()
    end_time = perf_counter()

    print(f'Tiempo transcurrido: {end_time-start:.2f} segundos')
