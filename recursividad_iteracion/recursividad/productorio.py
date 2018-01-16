import unittest
import math


class TestProductorio(unittest.TestCase):
    def test_productorio(self):
        n = 5
        resultado = productorio(n)
        self.assertEqual(resultado, 32768)


def productorio(n):
    if (n == 0):
        return 1
    return productorio(n - 1) * math.pow(2, n)
