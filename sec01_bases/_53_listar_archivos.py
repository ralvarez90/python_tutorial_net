"""LISTAR ARCHIVOS

Empleando la función walk podemos listar elementos dentro
de un sistema de ficheros.
"""
from pathlib import Path
from time import perf_counter
import os


def walk_obtener_rutas_imagenes():
    # home del usuario
    homePath = Path.home()

    # lista de imagenes
    png_imagenes = []

    # recorremos cada uno de los directorios
    for dirpath, dirnames, filenames in os.walk(homePath):
        for filename in filenames:
            if filename.endswith('.png') or filename.endswith('.jpg'):
                png_imagenes.append(os.path.join(dirpath, filename))

    # listamos archivos png
    print(f'total de imágenes: {len(png_imagenes)}')


def show_example_01():
    # conteo de inicio
    inicio = perf_counter()

    # ejecuta algorigmo
    walk_obtener_rutas_imagenes()

    # reporte
    print(f'Tiempo de ejecución: {perf_counter()-inicio:.2f}')


def main():
    show_example_01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
