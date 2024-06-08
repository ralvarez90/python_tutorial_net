"""ACCESORIOS DE PRUEBAS

Los test fixtures pueden ser métodos de clase. Estos son setUpClass y
tearDownloadClass.

Se puedne combinar con los test fixtures que setupUpModule y
teadDownModule.  El orden de ejecución sería.

setUpModule
setUpClass
    test unitario
    ...
tearDownClass
tearDownModule
"""
import unittest


def setUpModule():
    print('Running setUpModule...')


def tearDownModule():
    print('Running tearDownModule...')


class TestMyModule(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Running setUpClass method...')

    @classmethod
    def tearDownClass(cls):
        print('Running tearDownClass method...')

    def testCase1(self):
        self.assertEqual(2, 1+1)

    def testCase2(self):
        self.assertEqual(5+5, 10)
