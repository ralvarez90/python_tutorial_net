"""SEMÁFOROS

Un semáforo de Python es una primitiva de sincronización que le permite 
controlar el acceso a un recurso compartido. 

Básicamente, un semáforo es un contador asociado con un bloque (lock) que 
limita la cantidad de subprocesos que pueden acceder a un recurso 
compartido simultáneamente.

Un semáforo ayuda a prevenir problemas de sincronización de subprocesos, 
como condiciones de carrera, donde varios subprocesos intentan acceder 
al recurso al mismo tiempo e interfieren con las operaciones de los demás.

Un semáforo mantiene una cuenta. Cuando un hilo quiere acceder al recurso 
compartido, el semáforo verifica el recuento.

Si el recuento es mayor que cero, lo disminuye y permite que el hilo acceda 
al recurso. Si el recuento es cero, el semáforo bloquea el hilo hasta que el 
recuento sea mayor que cero.
"""
import threading
import urllib.request

MAX_CONCURRENT_DOWNLOADS = 3
semaphore = threading.Semaphore(value=MAX_CONCURRENT_DOWNLOADS)


def download(url: str):
    with semaphore:
        print('Downloading %s. . . ' % (url))
        response = urllib.request.urlopen(url)
        data = response.read()
        print('Finished downloading %s' % (url))
        return data


def main():
    # URLs to download
    urls = [
        'https://www.ietf.org/rfc/rfc791.txt',
        'https://www.ietf.org/rfc/rfc792.txt',
        'https://www.ietf.org/rfc/rfc793.txt',
        'https://www.ietf.org/rfc/rfc794.txt',
        'https://www.ietf.org/rfc/rfc795.txt',
    ]

    # list of threads
    threads = []

    # add threads in list, and started threads
    for url in urls:
        thread = threading.Thread(target=download, args=(url, ))
        threads.append(thread)
        thread.start()

    [t.join() for t in threads]


if __name__ == '__main__':
    main()
