"""DEAMON THREADS

En ocasiones es necesario ejecutar tareas en background. Existe un tipo
especial de thread denominado deamon thread. 

Por definición, los deamon threads son subprocesos en segundo plano. 
En otras palabras, los deamon threads ejecutan tareas en segundo plano.

Son útiles para ejecutar tareas que admiten threads normales pero en
background. Por ejemplo:

- Registrar información en un archivo en segundo plano.
- Eliminar contenidos de un sitio web en segundo plano.
- Guardar automáticamente los datos en una base de datos 
en segundo plano.

De igual forma empeamos la clase Thread pero usamos el parámetro
deamon en true.
"""
from threading import Thread
import time


def showExample01():

    # print counter per seconds
    def showTimer():
        count = 0
        while True:
            count += 1
            time.sleep(1)
            print('Has bee waiting for %d second(s)...' % (count))

    # make thread and start
    t = Thread(target=showTimer, daemon=True)
    t.start()

    input('\nDo you want to exit? \n')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
