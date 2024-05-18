"""THREADING LOOK

1. Condiciones de carrera
Una condición de carrera ocurre cuando 2 o más threads acceden o
pretenden acceder a una misma variable compartida.

Consiste en que ambos hilos intentan cambiar el valor de la variable 
compartida. Dado que las actualizaciones ocurren simultáneamente, 
se crea una carrera para determinar qué modificación del hilo 
se conserva.

El valor final de la variable compartida depende de qué hilo completa 
su actualización en último lugar. Cualquier hilo que cambie el valor 
en último lugar ganará la carrera.
"""
from threading import Thread
from time import perf_counter


def showExample01():
    pass


def main():
    showExample01()


if __name__ == '__main__':
    main()
