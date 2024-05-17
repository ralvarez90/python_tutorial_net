"""RETORNO DE VALORES

Podemos almacenar valores en instancias de que extienden
de clases que extienden a Thread.

Para regresar valores a partir de un thread, se extiende
entonces la clase Thread, y se almacena dicho valor en la
instancia de la clase.
"""
from threading import Thread
import urllib.error
import urllib.request


def showExample01():

    # inner class
    class HttpRequestThread(Thread):
        def __init__(self, url: str) -> None:
            super().__init__()
            self.url = url
            self.httpSatusCode = None
            self.reason = None

        def run(self) -> None:
            try:
                response = urllib.request.urlopen(self.url)
                self.httpSatusCode = response.code
            except urllib.error.HTTPError as e:
                self.httpSatusCode = e.code
            except urllib.error.URLError as e:
                self.reason = e.reason

        def __str__(self) -> str:
            return f'{self.url}: {self.httpSatusCode}'

    # make url list
    urls = [
        'https://httpstat.us/200',
        'https://httpstat.us/400'
    ]

    # create threads
    threadsToExec = [HttpRequestThread(url) for url in urls]

    # start threds and wait for the threads to complete
    [t.start() for t in threadsToExec]
    [t.join() for t in threadsToExec]

    # display properties
    [print(t) for t in threadsToExec]


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
