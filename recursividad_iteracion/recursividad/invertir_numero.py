import unittest
import math

class TestInvertirNumero(unittest.TestCase):
    def test_invertir_numero(self):
        numero = 123
        numero_invertido = invertir_numero(numero)
        print(numero_invertido)
        self.assertEqual(numero_invertido, 321)


def invertir_numero(numero):
    print(numero)
    if(numero < 10):
        return numero

