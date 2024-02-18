"""OPERACIONES ENTRE SETS

Podemos operar sets como en la teoría de conjuntos. Podemos
generar la union, intersección, diferencia, etc. Estos
se puden invocar como métodos union, intersection, etc
o se pueden realizar mediante operadores sobrecargados.

union (|)
Retorna la unión entre dos conjuntos

intersección (&)
Retorna la intersección entre dos conjuntos

diferencia (-)
Retorna la diferencia entre dos conjuntos

diferencia simétrica (^)
Retorna la diferencia simétrica entre dos
conjuntos.

issubset (<=)
Se emplea para verificar si un conjunto es subconjunto
de otro.

(<)
Se emplea para verificar si un conjunto es subconjunto propio
de otro.

issuperset (>=)
Verifica si un conjunto es superconjunto de otro, es decir, si
todos los elementos de un conjunto están dentro del segundo.

isdisjoint
Verifica si dos conjuntos son disjuntos, es decir, si su
intersección es vacía.
"""


def operacionesEjemplos():
    a = {1, 2, 3}
    b = {2, 3, 4}
    print(f'Si a={a}')
    print(f'Si b={b}')
    print(f'a | b -> {a|b}')
    print(f'a & b -> {a&b}')
    print(f'a - b -> {a-b}')
    print(f'a ^ b -> {a^b}')


if __name__ == '__main__':

    # run examples
    operacionesEjemplos()

    # end application
    input('\nPress any key to continue . . . ')
