"""DIRECTORIOS

os.getcwd()
Retorna el directorio actual donde el script de python se está
ejecutando.

os.chdir()
Nos permite movernos de directorio actual.

os.path.join()
Recibe una serie de strings y retorna una ruta de acuerdo al
sistema operativo desde el cual se invoca.

os.path.split()
Retorna una tupla de la forma (head, tail), donde la cola es el
ultimo elemento de la ruta.

os.path.isdir()
Retorna un booleano indicando si el path que recibe es un directorio.

os.path.mkdir()
Empleamos mkdir para crear un directorio en la ruta especificada, se
recomienda siempre verifiar que el directorio donde se piensa crear el
directorio exista.
"""
from pathlib import Path
import os
import time


def showExample01():
    # home de usuario
    userPath = Path.home()

    # directorio actual
    actualDir = os.getcwd()
    print('Directorio actual: %s' % (actualDir))

    # nos movemos a directorio de usuario
    os.chdir(userPath)
    homeFiles = os.listdir(userPath)

    # show normal files and dires
    [print(f) for f in homeFiles if not f.startswith('.')]


def showExample02():
    homePath = Path.home()
    completePath = os.path.join(homePath, 'snap')
    print(f'{completePath}')
    directoriosDelPath = os.path.split(completePath)
    print(directoriosDelPath)


def isDirectory(path: str) -> bool:
    return os.path.exists(path) or os.path.isdir(path)


def showExample03():
    snapDirPath = os.path.join(Path.home(), 'snap')
    print(f'{snapDirPath} is a directory: {isDirectory(snapDirPath)}')


def showExample04():
    dirActual = os.getcwd()
    dirTemporal = os.path.join(dirActual, 'temporal')

    if not os.path.exists(dirTemporal):
        os.mkdir(dirTemporal)

    print('Esperamos...')
    time.sleep(5)
    if os.path.exists(dirTemporal):
        os.rmdir(dirTemporal)
        print(f'{dirTemporal}  eliminado...')


def main():
    # show_example_1()
    showExample02()
    showExample03()
    showExample04()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue. . .')
