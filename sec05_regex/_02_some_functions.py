"""MÉTODOS COMÚNES

Dado un Pattern obtenido a partir de re.compile, disponemos de diferentes
métodos para el manejo de expresiones regulares.

1. findall
Retorna una lista de todas las coincidencias del patrón en el string.

2. match
Encuentra un patrón al inicio de string.

3. search
Retorna la primera coincidencia del patrón en el string.

4. finditer
Retorna todas las incidencias del patrón como un iterador.

Usar las funciones del módulo re es más conciso que los 
métodos del objeto Pattern porque no es necesario compilar 
expresiones regulares manualmente.

En esencia, estas funciones crean un objeto Pattern y llaman 
al método apropiado en él. También almacenan la expresión 
regular compilada en un caché para optimizar la velocidad.

Significa que si llama a la misma expresión regular la segunda 
vez, estas funciones no necesitarán volver a compilar 
la expresión regular. En cambio, obtienen la expresión regular 
compilada del caché.

Si utiliza una expresión regular dentro de un bucle, el objeto 
Patter puede guardar algunas llamadas a funciones. Sin embargo, 
si lo usas fuera de bucles, la diferencia es muy pequeña debido 
al caché interno.
"""
import re


def showExample01():
    print('Example 01. Using re.findall')
    s = 'Python 3.10 was released on October 04, 2021.'
    results = re.findall(r'\d', s)
    print(results)


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
