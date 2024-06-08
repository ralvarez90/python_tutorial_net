"""ACCESORIOS DE TESTS

Por definición un test fixture (accesorio de pruba) es una función 
o método que ejecuta bloques de código antes o después de efectuar
pruebas unitarias.

Si agrega las funciones setUpModule y tearDownModule, estas sejecuta
antes y después de realziar todas las pruebas.
"""
import unittest


def setUpModule():
    print('Running setUpModule')


def tearDownModule():
    print('Running tearDownloadModule')


class TestMyModule(unittest.TestCase):

    def testCase1(self):
        self.assertEqual(10, 5+5)

    def testCase2(self):
        self.assertEqual(2+1, 3)
