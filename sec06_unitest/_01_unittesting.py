"""UNIT TEST

En primera instancia se emplea el módulo unittest para probar unidades
de código.

Se suele crear una clase de prueba por cada clase construida y un método
de prueba por cada clase.
"""
import unittest


class Square:
    def __init__(self, length: int) -> None:
        self.length = length

    def area(self):
        return self.length ** 2


class TestSquare(unittest.TestCase):

    def testArea(self):
        square = Square(10)
        self.assertEqual(square.area(), 100)


if __name__ == '__main__':
    # si se omite -m unittest al ejecutar script se puede
    # omitir la siguiente validación.
    # unittest.main()
    pass
