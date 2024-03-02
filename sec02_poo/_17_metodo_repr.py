"""MÉTODO __repr__

Funciona de forma similar al __str__, este define el comportamiento
cuando pasa una instancia de una clase al método repr().

El método __repr__ regresa un string representativo de un objeto, donde
regularmente se retorna un string que puede ser ejecutado por el método
eval.

Cuando una clase no tiene implementado el método __str__ y se imprime, 
utiliza el string devuelto por __repr__ por default.

El método __str__ devuelve una representación de cadena de un objeto 
legible por humanos, mientras que el método __repr__ devuelve una 
representación de cadena de un objeto legible por máquina.
"""
