"""THREAD LOOK

Para prevenir condiciones de carrera se emplea el concepto
de threading look (bloqueo de hilo).

Un bloqueo de subprocesos (bloque de hilos o thread look) es una 
primitiva de sincronización que proporciona acceso exclusivo a un 
recurso compartido en una aplicación multiproceso. 

Un bloqueo de subprocesos (thread look) también se conoce como mutex, 
que es la abreviatura de exclusión mutua.

Normalmente, un bloqueo de subprocesos tiene dos estados: bloqueado y 
desbloqueado. Cuando un hilo adquiere un lock, el lock entra en el 
estado bloqueado. El hilo puede tener acceso exclusivo al recurso compartido.

Otros subprocesos que intenten adquirir el bloqueo mientras está 
bloqueado serán bloqueados y esperarán hasta que se libere el bloqueo.

En Python, puedes usar la clase Lock del módulo de subprocesamiento 
para crear un objeto de bloqueo:
"""
from threading import Thread, Lock
from time import sleep

# counter global variable
counter: int = 0


def increase(by: int, lock: Lock):
    global counter

    # adquiere bloqueo
    lock.acquire()

    localCounter = counter
    localCounter += by
    sleep(0.1)
    counter = localCounter
    print('counter=%d' % (counter))

    # release bloqueo
    lock.release()


def main():

    # get look instance
    lock = Lock()

    # create threads
    threadTask = [Thread(target=increase, args=(i, lock))
                  for i in range(1, 11)]

    # start tasks
    [f.start() for f in threadTask]

    # add to main thread
    [f.join() for f in threadTask]

    print('Final counter: %d' % (counter))


if __name__ == '__main__':
    main()
