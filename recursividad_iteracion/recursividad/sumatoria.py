import unittest
import math


class TestSumatoria(unittest.TestCase):
    def test_sumatoria(self):
        n = 5
        resultado = sumatoria(n)
        self.assertEqual(resultado, 63)


def sumatoria(n):
    if (n == 0):
        return 1
    return sumatoria(n - 1) + math.pow(2, n)
