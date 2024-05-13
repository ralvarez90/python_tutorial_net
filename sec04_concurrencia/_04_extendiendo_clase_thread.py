"""EXTENDIENDO LA CLASE THREAD

Cuando un programa inicia, este tiene un thread principal
llamado main thread. 

Uno de las formas para ejecutar código dentro de nuevo thread es
extender a clase Thread.

1- Se define una subclase de threading.Thread
2. Se sobrescribe el método __init__
3. Se sobrescribe el método run
"""
from threading import Thread
import urllib.error
import urllib.request


class HttpRequestThread(Thread):
    def __init__(self, url: str) -> None:
        super().__init__()
        self.url = url

    def run(self) -> None:
        print(f'Checking {self.url}')
        try:
            response = urllib.request.urlopen(self.url)
            print(response.code)
        except urllib.error.HTTPError as e:
            print(e.code)
        except urllib.error.URLError as e:
            print(e.reason)


def showExample01():
    urls = [
        'https://httpstat.us/200',
        'https://httpstat.us/400'
    ]

    threads = [HttpRequestThread(url) for url in urls]
    [t.start() for t in threads]
    [t.join() for t in threads]


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
