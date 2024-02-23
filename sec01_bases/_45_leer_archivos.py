"""LECTURA DE ARCHIVOS

El leer un archivo en python conlleva los siguientes
elementos:
- Abrir un archivo de texto para lectura empleando la función
open.
- Leer el contenido del archivo de texto empleando los
métodos read, readline o readlines del objeto file que retorna
la función open.
- Cerrar el archivo empleando el método close.

1. Función open
Puede recibir diversos parámetros pero los principales son:
- path (ruta del archivo), este si se encuentra localizado
dentro del mismo directorio del script que ejecuta python
únicamente se requiere poner el nombre del archivo.
- mode (modo en el que se abre el archivo), este parámetro
es opcional:
r   modo lectura
w   modo escritura
a   modo escritura agregando el contenido al final del archivo.

2. Close
Método importante de ejecutar ya que usualmente al ejecutar
abrir un archivo el sistema operativo suele bloquear el 
archivo para que ningún otro proceso pueda modificar el
archivo.

Otra razón es que el sistema de archivos tiene una cantidad
limitada de file-dscriptors (descriptores de archivos) que 
puede crear antes de que se agoten. Es posible agotar los
recursos de archivos al abrir MUCHOS archivos.

Dejar muchos archivos abiertos puede provocar condiciones
de carrera
"""


if __name__ == '__main__':
    pass
