import unittest

"""USO DE TESTS

assertEqual
Asegura el igual en los test.

assertRaiser
Se asegura que las funciones en cuestión lanze difeentes
tipos de excepiones.
"""


class Square:

    def __init__(self, length: int | float):
        if type(length) not in (int, float):
            raise TypeError('Length must be an integer of float')

        if length < 0:
            raise ValueError('Length can be a negative integer.')

        self.length = length

    def area(self) -> int | float:
        return self.length ** 2


class TestSquare(unittest.TestCase):

    def testArea(self):
        self.assertEqual(Square(10).area(), 100)

    def testLengthWrongType(self):
        with self.assertRaises(TypeError):
            Square('10')

    def testLengthNegative(self):
        with self.assertRaises(ValueError):
            Square(-1) | Square(0)
