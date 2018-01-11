import unittest

class TestBubbleSort(unittest.TestCase):

    def test_caso_mejor_1(self):
        array = self.get_array(1, 'mejor')
        self.bubble_sort(array)
        self.assertEqual(0, 0)

    def test_caso_mejor_2(self):
        array = self.get_array(2, 'mejor')
        self.bubble_sort(array)
        self.assertEqual(0, 0)

    def test_caso_mejor_3(self):
        array = self.get_array(3, 'mejor')
        self.bubble_sort(array)
        self.assertEqual(0, 0)

    def test_caso_mejor_4(self):
        array = self.get_array(4, 'mejor')
        self.bubble_sort(array)
        self.assertEqual(0, 0)

    def test_caso_mejor_5(self):
        array = self.get_array(5, 'mejor')
        self.bubble_sort(array)
        self.assertEqual(0, 0)

    def test_caso_peor_1(self):
        array = self.get_array(1, 'peor')
        self.bubble_sort(array)
        self.assertEqual(0, 0)

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
        n = len(numeros) - 1
        for j in range(0, n):
            for i in range(0, n-j):
                if numeros[i] > numeros[i+1]:
                    temporal = numeros[i]
                    numeros[i] = numeros[i+1]
                    numeros[i + 1] = temporal

    def get_array(self, case, notation):
        file = open('../files/' + str(case) + '/' + str(case) + str(notation) +'.txt')
        data = file.read()
        file.close()
        return [int(n) for n in data.split(',')]

if __name__ == '__main__':
    unittest.main()