"""PROCESOS Y THREADS

Por definición, un proceso es una instancia de un programa que se ejecuta en 
una computadora. Y un hilo (thread) es una unidad de ejecución dentro de un
proceso.

Un programa es como una clase, mientras que los procesos son como objetos de 
la clase.
"""
from time import sleep, perf_counter


def runTask(id: int):
    print(f'Starting task {id}...')
    sleep(1)
    print(f'Done task {id}')


def main():
    # inicio temporizador
    ti = perf_counter()

    # ejecuta tareas sincronas
    for idTask in range(10):
        runTask(id=idTask)

    # resultados
    deltaT = perf_counter() - ti
    print(f'It took {deltaT: 0.2f} second(s) to complete')


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
