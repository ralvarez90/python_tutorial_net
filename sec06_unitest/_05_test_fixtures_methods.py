"""TEST FIXTURES METHODS

Además de los test fixtures de modulo, y de métodos de clase
podemos agregar los métodos de instancia setUp y tearDown dentro
de una clase de pruebas.

setUp y tearDown se ejecuta antes y después de cada prueba
unitaria dentro de la clase.
"""
import unittest


def setUpModule():
    print('Running setUpModule')


def tearDownModule():
    print('Running tearDownModule')


class TestMyModule(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Running setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('Running tearDownClass')

    def setUp(self):
        print('')
        print('Running setUp')

    def tearDown(self):
        print('Running tearDown')

    def test_case_1(self):
        print('Running test_case_1')
        self.assertEqual(5+5, 10)

    def test_case_2(self):
        print('Running test_case_2')
        self.assertEqual(1+1, 2)
