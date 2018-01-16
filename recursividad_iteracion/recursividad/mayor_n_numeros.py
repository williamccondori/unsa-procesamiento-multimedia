import unittest


class TestMayorNnumeros(unittest.TestCase):
    def test_mayor_n_numeros(self):
        array = [2, 34, 5, 2, 22, 34, 5, 7, 4, 3, 100]
        mayor = mayor_n_numeros(array)
        print(mayor)
        self.assertEqual(mayor, 100)


def mayor_n_numeros(array):

    if(len(array) == 1):
        return array[0]

    mitad = (int)(len(array) / 2)
    array_izquierda=array[mitad:]
    array_derecha=array[:mitad]

    mayor_izquierda = mayor_n_numeros(array_izquierda)
    mayor_derecha = mayor_n_numeros(array_derecha)

    if(mayor_izquierda > mayor_derecha):
        return mayor_izquierda
    else:
        return mayor_derecha
