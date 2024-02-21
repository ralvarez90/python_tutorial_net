"""PACKAGES

Los paquetes son grupos de módulos almacenados en
carpetas. Los paquetes permiten organizar módulos
en una estructura jerárquica.

__init__.py
Para crear un paquete, cree un nuevo folder con al
menos un archivo python __init__.py, aunque a partir de
python 3.3 cualquier folder se puede tratar como
paquete.

Por convención, cuando se importa un paquete se ejecuta
el script __init__.py de dicho paquete, esto permite
inicializar elementos a nivel de paquete en el momento
que se importa.

Para import un módulo contenido dentro de un paquete
se emplea la sentencia:
import paquete.modulo

Para crear código más conciso puede importar objetos
de módulos dentro deun paquete de la forma
from paquete.modulo import objeto

Además de inicializar datos a nivel de paquete, __init__.py 
también le permite importar módulos automáticamente 
desde el paquete.

from <package> import *
Si se importa todo el módulo con esta sentencia, si el archivo
__init__.py existe, cargará todos los módulos especificados en 
una lista especial llamada __all__ en el archivo.
"""
