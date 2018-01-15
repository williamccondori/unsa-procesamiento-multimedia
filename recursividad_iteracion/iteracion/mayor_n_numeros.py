import unittest


class TestMayorNnumeros(unittest.TestCase):
    def test_mayor_n_numeros(self):
        array = [2, 4, 5, 2, 4, 8, 54, 7, 4, 3]
        mayor = mayor_n_numeros(array)
        self.assertEqual(mayor, 54)


def mayor_n_numeros(array):
    mayor = 0
    for i in range(0, len(array)):
        if (array[i] > mayor):
            mayor = array[i]
    return mayor
