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


def main():
    # conteo de inicio
    inicio = perf_counter()

    # ejecuta algorigmo
    walkObtenerRutasImagenes()

    # reporte
    print(f'Tiempo de ejecución: {perf_counter()-inicio:.2f}')


if __name__ == '__main__':
    # run application
    main() or input('\nPress any key to continue . . .')
