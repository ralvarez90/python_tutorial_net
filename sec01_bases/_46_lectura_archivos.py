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


def obtenerListaDeArchivos(path: str = './') -> list[str]:
    """Obtiene lista de archivos del directorio actual por default. Puede
    espeficicar cualquier path del sistema.
    """
    actual_path = (os.getcwd(), path)[path != '']
    if os.path.isdir(actual_path):
        return os.listdir(actual_path)
    return []


def main():
    archivos = sorted(obtenerListaDeArchivos())
    unArchivo = random.choice(archivos)
    if unArchivo != '':
        with open(file=unArchivo, mode='r', encoding='utf-8') as f:
            for line in f:
                print(line.strip())
    else:
        print('Sin archivos en directorio: %s' % (unArchivo))


if __name__ == '__main__':

    # run application
    main()

    # end message
    input('\nPress any key to continue. . .')
