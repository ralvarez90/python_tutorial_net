"""THREADING EVENT OBJECT

A veces, es necesario comunicarse entre hilos. Para hacer eso, 
puedes usar un bloqueo (mutex) y una variable booleana, sin embargo, 
Python le proporciona una mejor manera de comunicarse entre 
subprocesos utilizando la clase Event del módulo de 
subprocesos.

La clase Event ofrece una manera simple pero efectiva de coordinar 
entre subproceso: un subproceso señala un evento mientras otros 
subprocesos lo esperan.

El objeto Event envuelve un indicador booleano que se puede 
establecer (Verdadero) o borrar (Falso). 

Varios subprocesos pueden esperar a que se establezca un 
evento antes de continuar o pueden restablecer el 
evento al estado borrado.

A continuación se ilustran los pasos para utilizar el 
objeto Event:

- Primero, importe el evento desde el módulo de subprocesamiento
- cree una instancia de Event, por default un evento está no
establecido, es decir está cleared, por lo que el método is_set
retorna False.
"""
from threading import Thread, Event
from time import sleep


def task(event: Event, id: int) -> None:
    print('Thread %d started. Waiting for the signal. . .' % (id))
    event.wait()
    print('Received signal. The thread %d was completed. . . ' % (id))


def main() -> None:

    # event instance
    event = Event()

    # create threads
    threads = [Thread(target=task, args=(event, i)) for i in range(1, 11)]
    [t.start() for t in threads]

    print('\n\nBlocking the main thread for 10 seconds. . . ')
    sleep(10)

    # set event
    event.set()


if __name__ == '__main__':
    main()
