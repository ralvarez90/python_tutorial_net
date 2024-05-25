"""THREADING LOOK

1. Condiciones de carrera
Una condición de carrera ocurre cuando 2 o más threads acceden o
pretenden acceder a una misma variable compartida.

Consiste en que ambos hilos intentan cambiar el valor de la variable 
compartida. Dado que las actualizaciones ocurren simultáneamente, 
se crea una carrera para determinar qué modificación del hilo 
se conserva.

El valor final de la variable compartida depende de qué hilo completa 
su actualización en último lugar. Cualquier hilo que cambie el valor 
en último lugar ganará la carrera.
"""
from threading import Thread
from time import sleep

# global counter
counter: int = 0


def increase(by: int):
    global counter

    localCounter = counter
    localCounter += by
    sleep(0.1)
    counter = localCounter
    print('counter=%d' % (counter))


def showExample01():
    global counter
    counter = 0

    # create threads
    threadsTasks = [Thread(target=increase, args=(i,)) for i in [10, 20]]

    # start thread tasks
    [f.start() for f in threadsTasks]
    [f.join() for f in threadsTasks]

    # final counter
    print('Final counter: %d' % (counter))


def main():
    for _ in range(100):
        showExample01()


if __name__ == '__main__':
    main()
