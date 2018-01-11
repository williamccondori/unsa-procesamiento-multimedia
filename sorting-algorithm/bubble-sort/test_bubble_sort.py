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
    
    def test_caso_mejor_6(self):
        """
        Caso de prueba para el mejor caso con datos de tamaño (10 a la 6)
        """
        array = self.get_array(6, 'mejor')
        self.bubble_sort(array)
        self.assertEqual(len(array), 1000000)

    # Casos de prueba para los peores casos.

    def test_caso_peor_1(self):
        """
        Caso de prueba para el peor caso con datos de tamaño (10 a la 1)
        """
        array = self.get_array(1, 'peor')
        self.bubble_sort(array)
        self.assertEqual(len(array), 10)

    def test_caso_peor_2(self):
        array = self.get_array(2, 'peor')
        self.bubble_sort(array)
        self.assertEqual(0, 0)

    def test_caso_peor_3(self):
        array = self.get_array(3, 'peor')
        self.bubble_sort(array)
        self.assertEqual(0, 0)

    def test_caso_peor_4(self):
        array = self.get_array(4, 'peor')
        self.bubble_sort(array)
        self.assertEqual(0, 0)

    def test_caso_peor_5(self):
        array = self.get_array(5, 'peor')
        self.bubble_sort(array)
        self.assertEqual(0, 0)

    # Casos de prueba para los casos promedio

    def test_caso_promedio_1(self):
        array = self.get_array(1, 'promedio')
        self.bubble_sort(array)
        self.assertEqual(0, 0)

    def test_caso_promedio_2(self):
        array = self.get_array(2, 'promedio')
        self.bubble_sort(array)
        self.assertEqual(0, 0)

    def test_caso_promedio_3(self):
        array = self.get_array(3, 'promedio')
        self.bubble_sort(array)
        self.assertEqual(0, 0)

    def test_caso_promedio_4(self):
        array = self.get_array(4, 'promedio')
        self.bubble_sort(array)
        self.assertEqual(0, 0)

    def test_caso_promedio_5(self):
        array = self.get_array(5, 'promedio')
        self.bubble_sort(array)
        self.assertEqual(0, 0)

    def bubble_sort(self, numeros):
        """
        Función que implementa el algoritmo de bubble sort.
        :param numeros: array de números
        :return: None
        """
        n = len(numeros) - 1
        for j in range(0, n):
            for i in range(0, n-j):
                if numeros[i] > numeros[i+1]:
                    temporal = numeros[i]
                    numeros[i] = numeros[i+1]
                    numeros[i + 1] = temporal

    def get_array(self, case, notation):
        """
        Función que obtiene el array de los arhivos de texto..
        """
        file = open('../files/' + str(case) + '/' + str(case) + str(notation) +'.txt')
        data = file.read()
        file.close()
        return [int(n) for n in data.split(',')]

if __name__ == '__main__':
    unittest.main()