"""
Se importa la librería para pruebas unitarias.
"""
import unittest


class TestBubbleSort(unittest.TestCase):
    """
    Clase que contiene los casos de prueba para bubble sort.
    """

    # Casos de prueba para los mejores casos.

    def test_caso_mejor_1(self):
        """
        Caso de prueba para el mejor caso con datos de tamaño (10 a la 1)
        """
        array = self.get_array(1, 'mejor')
        self.bubble_sort(array)
        self.assertEqual(len(array), 10)

    def test_caso_mejor_2(self):
        """
        Caso de prueba para el mejor caso con datos de tamaño (10 a la 2)
        """
        array = self.get_array(2, 'mejor')
        self.bubble_sort(array)
        self.assertEqual(len(array), 100)

    def test_caso_mejor_3(self):
        """
        Caso de prueba para el mejor caso con datos de tamaño (10 a la 3)
        """
        array = self.get_array(3, 'mejor')
        self.bubble_sort(array)
        self.assertEqual(len(array), 1000)

    def test_caso_mejor_4(self):
        """
        Caso de prueba para el mejor caso con datos de tamaño (10 a la 4)
        """
        array = self.get_array(4, 'mejor')
        self.bubble_sort(array)
        self.assertEqual(len(array), 10000)

    def test_caso_mejor_5(self):
        """
        Caso de prueba para el mejor caso con datos de tamaño (10 a la 5)
        """
        array = self.get_array(5, 'mejor')
        self.bubble_sort(array)
        self.assertEqual(len(array), 100000)

    def caso_mejor_6(self):
        """
        Caso de prueba para el mejor caso con datos de tamaño (10 a la 6)
        """
        array = self.get_array(6, 'mejor')
        self.bubble_sort(array)
        # self.assertEqual(len(array), 1000000)

    # Casos de prueba para los peores casos.

    def test_caso_peor_1(self):
        """
        Caso de prueba para el peor caso con datos de tamaño (10 a la 1)
        """
        array = self.get_array(1, 'peor')
        self.bubble_sort(array)
        self.assertEqual(len(array), 10)

    def test_caso_peor_2(self):
        """
        Caso de prueba para el peor caso con datos de tamaño (10 a la 2)
        """
        array = self.get_array(2, 'peor')
        self.bubble_sort(array)
        self.assertEqual(len(array), 100)

    def test_caso_peor_3(self):
        """
        Caso de prueba para el peor caso con datos de tamaño (10 a la 3)
        """
        array = self.get_array(3, 'peor')
        self.bubble_sort(array)
        self.assertEqual(len(array), 1000)

    def test_caso_peor_4(self):
        """
        Caso de prueba para el peor caso con datos de tamaño (10 a la 4)
        """
        array = self.get_array(4, 'peor')
        self.bubble_sort(array)
        self.assertEqual(len(array), 10000)

    def caso_peor_5(self):
        """
        Caso de prueba para el peor caso con datos de tamaño (10 a la 5)
        """
        array = self.get_array(5, 'peor')
        self.bubble_sort(array)
        self.assertEqual(len(array), 100000)

    def caso_peor_6(self):
        """
        Caso de prueba para el peor caso con datos de tamaño (10 a la 6)
        """
        array = self.get_array(6, 'peor')
        self.bubble_sort(array)
        self.assertEqual(len(array), 1000000)

    # Casos de prueba para los casos promedio.

    def test_caso_promedio_1(self):
        """
        Caso de prueba para el caso promedio con datos de tamaño (10 a la 1)
        """
        array = self.get_array(1, 'promedio')
        self.bubble_sort(array)
        self.assertEqual(len(array), 10)

    def test_caso_promedio_2(self):
        """
        Caso de prueba para el caso promedio con datos de tamaño (10 a la 2)
        """
        array = self.get_array(2, 'promedio')
        self.bubble_sort(array)
        self.assertEqual(len(array), 100)

    def test_caso_promedio_3(self):
        """
        Caso de prueba para el caso promedio con datos de tamaño (10 a la 3)
        """
        array = self.get_array(3, 'promedio')
        self.bubble_sort(array)
        self.assertEqual(len(array), 1000)

    def test_caso_promedio_4(self):
        """
        Caso de prueba para el caso promedio con datos de tamaño (10 a la 4)
        """
        array = self.get_array(4, 'promedio')
        self.bubble_sort(array)
        self.assertEqual(len(array), 10000)

    def caso_promedio_5(self):
        """
        Caso de prueba para el caso promedio con datos de tamaño (10 a la 5)
        """
        array = self.get_array(5, 'promedio')
        self.bubble_sort(array)
        self.assertEqual(len(array), 100000)

    def caso_promedio_6(self):
        """
        Caso de prueba para el caso promedio con datos de tamaño (10 a la 6)
        """
        array = self.get_array(6, 'promedio')
        self.bubble_sort(array)
        self.assertEqual(len(array), 1000000)

    # Algoritmo de ordenación.

    def bubble_sort(self, numeros):
        """
        Función que implementa el algoritmo de bubble sort.
        :param numeros: array de números
        """
        total = len(numeros)
        for j in range(0, total):
            ordenado = True
            for i in range(0, total-j-1):
                if numeros[i] > numeros[i+1]:
                    numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]
        # print(numeros)

    def get_array(self, case, notation):
        """
        Función que obtiene el array de los arhivos de texto..
        """
        try:
            ruta = 'files/' + str(case) + '/' + str(case) + str(notation) +'.txt'
            file = open(ruta)
            data = file.read()
            file.close()
            array = [int(n) for n in data.split(',')]
            return array
        except Exception as identifier:
            print(identifier)
            return []

if __name__ == '__main__':
    unittest.main()
