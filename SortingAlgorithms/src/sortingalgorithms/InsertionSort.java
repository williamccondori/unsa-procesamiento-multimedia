package sortingalgorithms;

public class InsertionSort {

    public int[] Ejecutar(int[] arreglo) {
        for (int i = 1; i < arreglo.length; ++i) {
            int mano = arreglo[i];
            int j = i - 1;
            while (j >= 0 && arreglo[j] > mano) {
                arreglo[j + 1] = arreglo[j];
                j = j - 1;
            }
            arreglo[j + 1] = mano;
        }
        return arreglo;
    }

    public static void main(String[] args) {
        Helper helper = new Helper();
        InsertionSort insertionSort = new InsertionSort();
        int[] numeros = helper.GenerarPeorCaso(3);
        long tiempoInicio = System.nanoTime();
        numeros = insertionSort.Ejecutar(numeros);
        long tiempoFin = System.nanoTime();
        helper.CalcularTiempo(tiempoInicio, tiempoFin);
        System.out.println("Tamaño: " + numeros.length);
    }

}
