package sortingalgorithms;

public class BubbleSort {

    public int[] Ejecutar(int[] arreglo) {
        boolean desordenado = true;
        for (int i = 0; i < arreglo.length; i++) {
            if (desordenado == true) {
                desordenado = false;
                for (int j = 0; j < arreglo.length - i - 1; j++) {
                    if (arreglo[j] > arreglo[j + 1]) {
                        int temp = arreglo[j];
                        arreglo[j] = arreglo[j + 1];
                        arreglo[j + 1] = temp;
                        desordenado = true;
                    }
                }
            }
        }
        return arreglo;
    }

    public static void main(String[] args) {
        Helper helper = new Helper();
        BubbleSort bubbleSort = new BubbleSort();
        int[] numeros = helper.GenerarPeorCaso(3);
        long tiempoInicio = System.nanoTime();
        numeros = bubbleSort.Ejecutar(numeros);
        long tiempoFin = System.nanoTime();
        helper.CalcularTiempo(tiempoInicio, tiempoFin);
        System.out.println("Tamaño: " + numeros.length);
    }

}
