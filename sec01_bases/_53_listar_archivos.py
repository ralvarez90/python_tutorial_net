"""LISTAR ARCHIVOS

Empleando la función walk podemos listar elementos dentro
de un sistema de ficheros.
"""
from pathlib import Path
from time import perf_counter
import os


def walkObtenerRutasImagenes():
    # home del usuario
    homePath = Path.home()

    # lista de imagenes
    pngImages = []

    # recorremos cada uno de los directorios
    for dirpath, dirnames, filenames in os.walk(homePath):
        for filename in filenames:
            if filename.endswith('.png') or filename.endswith('.jpg'):
                pngImages.append(os.path.join(dirpath, filename))

    # listamos archivos png
    print(f'total de imágenes: {len(pngImages)}')


def showExample01():
    # conteo de inicio
    ti = perf_counter()

    # ejecuta algorigmo
    walkObtenerRutasImagenes()

    # reporte
    tf = perf_counter()
    deltaT = abs(tf-ti)
    print(f'Tiempo de ejecución: {deltaT:.2f} seg')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
