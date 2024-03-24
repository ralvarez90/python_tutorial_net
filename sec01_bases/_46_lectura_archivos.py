"""LECTURA DE ARCHIVOS

Empleamos de igual forma la función open con el modo
r. Este permite leer información sin permisos de 
escritura.

Para leer texto con utf-8, a la función open se le
requiere especificar el argumento encoding.
"""
from _45_escritura_archivos import *
import os
import random


def getFileList(path: str = './') -> list[str]:
    """Obtiene lista de archivos del directorio actual por default. Puede
    espeficicar cualquier path del sistema.
    """
    actualPath = (os.getcwd(), path)[path != '']
    if os.path.isdir(actualPath):
        return os.listdir(actualPath)
    return []


def showExample01():
    archivos = sorted(getFileList())
    unArchivo = random.choice(archivos)
    if unArchivo != '':
        with open(file=unArchivo, mode='r', encoding='utf-8') as f:
            for line in f:
                print(line.strip())
    else:
        print('Sin archivos en directorio: %s' % (unArchivo))


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue. . .')
