"""ITERADORES

Un iterador es un objeto cuya clase implementa los métodos:
__iter__
    Retorna el objeto en cuestrión
    
__next__
    Retorna un siguiente elemento

Una vez que se iteran por todos los elementos, el iterador es
consumido, por lo que requeriría crear otro objeto iterador
para volver a recorrerlo.

Si se intenta usar nuevamente un iterador ya agotardo se lanzará
un StopIteration exception.

Notas:
- Estos dos métodos permiten implementar el protocolo de iteración,
es decir, cualquier clase que implemente dichos métodos, cumplirá
con dicho protocolo y por ende sus instancias serán iteradores.
"""


class Square:
    def __init__(self, length: int) -> None:
        assert length < 0, 'The length cannot be a negative number'
        self.length = length
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.length:
            raise StopIteration
        self.current += 1
        return self.current ** 2


def showExample01():
    print('EXAMPLE 01. Get Square Iterator')
    square = Square(length=5)
    for sq in square:
        print(sq)


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
