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
    pngImages = []

    # recorremos cada uno de los directorios
    for dirpath, dirnames, filenames in os.walk(homePath):
        for filename in filenames:
            if filename.endswith('.png') or filename.endswith('.jpg'):
                pngImages.append(os.path.join(dirpath, filename))

    # listamos archivos png
    print(f'total de imágenes: {len(pngImages)}')


def show_example_1():
    # conteo de inicio
    inicio = perf_counter()

    # ejecuta algorigmo
    walk_obtener_rutas_imagenes()

    # reporte
    print(f'Tiempo de ejecución: {perf_counter()-inicio:.2f}')


def main():
    show_example_1()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . .')
