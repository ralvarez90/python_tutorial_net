"""HOW STOP A THREAD IN PYTHON

1. Clase Event
Para detener un subproceso puede usar un objeto Event. Esta clase
cuenta con una bandera booleana thread safe que puede ser establecida
como verdadera, por default es False.

El método set establece la bandera interna en True mientras que
clear en False.

Para detener un subproceso dentro del main thread usando un objeto
Event se requiere:
- Crear un nuevo Event y pasarlo como parámetro al thread hijo.
- De forma periódica verificar el estado interno del objeto
empleando is_set() y detenerlo si la bandera interna ha sido
establecida.
"""
from threading import Thread, Event
from time import sleep


def task(event: Event):
    for i in range(6):
        print('Running #%d' % (i+1))
        sleep(1)
        if event.is_set():
            print('The thread was stopped prematurely.')
            break
    else:
        print('The thread wast stopped maturely.')


def main():

    # create event and thread
    event = Event()
    thread = Thread(target=task, args=(event, ))

    # start thread
    thread.start()

    # suspend the thread after 3 seconds
    sleep(3)
    event.set()


if __name__ == '__main__':
    main()
