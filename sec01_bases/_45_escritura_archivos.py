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
de carrera.

Notas:
- Si se usa el + en el especificador de modo, se puede 
leer y escribir.
"""
# import this
import textwrap


def crearZenPythonFile():

    s = textwrap.dedent(
        """\
        Gur Mra bs Clguba, ol Gvz Crgref
        Ornhgvshy vf orggre guna htyl.
        Rkcyvpvg vf orggre guna vzcyvpvg.
        Fvzcyr vf orggre guna pbzcyrk.
        Pbzcyrk vf orggre guna pbzcyvpngrq.
        Syng vf orggre guna arfgrq.
        Fcnefr vf orggre guna qrafr.
        Ernqnovyvgl pbhagf.
        Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
        Nygubhtu cenpgvpnyvgl orngf chevgl.
        Reebef fubhyq arire cnff fvyragyl.
        Hayrff rkcyvpvgyl fvyraprq.
        Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
        Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
        Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
        Abj vf orggre guna arire.
        Nygubhtu arire vf bsgra orggre guna *evtug* abj.
        Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
        Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
        Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!
        """
    )

    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(i+c)] = chr((i+13) % 26 + c)

    resultados = ''.join([d.get(c, c) for c in s])

    # almacenamos en archivo
    f = open('zen_python.txt', mode='w')
    f.write(resultados)
    f.close()

    # ejemplo de de uso con context manager, solo ejecuta
    # el close.
    # with open('zen_python.txt', mode='w') as f:
    #     f.write(resultados)


if __name__ == '__main__':

    # run application
    crearZenPythonFile()

    # end message
    input('\nPress any key to continue . . .')
