"""PROCESOS Y THREADS

Por definición, un proceso es una instancia de un programa que se ejecuta en 
una computadora. Y un hilo (thread) es una unidad de ejecución dentro de un
proceso.

Un programa es como una clase, mientras que los procesos son 
como objetos de la clase.
"""
from time import sleep, perf_counter



def showExample01():

    # inner function
    def task():
        print(f'starting task...')
        sleep(1)
        print(f'done')

    ti = perf_counter()
    for _ in range(5):
        task()
    tf = perf_counter()
    print(f'Tiempo transcurrido: {tf-ti:.2f} segundos')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
