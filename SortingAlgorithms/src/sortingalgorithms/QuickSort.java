package sortingalgorithms;

public class QuickSort {

    int Partition(int arreglo[], int inicio, int fin) {
        int x = arreglo[fin];
        int i = (inicio - 1);
        for (int j = inicio; j <= fin - 1; j++) {
            if (arreglo[j] <= x) {
                i++;
                int temp = arreglo[i];
                arreglo[i] = arreglo[j];
                arreglo[j] = temp;
            }
        }
        int temp = arreglo[i + 1];
        arreglo[i + 1] = arreglo[fin];
        arreglo[fin] = temp;
        return (i + 1);
    }

    int[] Ejecutar(int[] arreglo, int inicio, int fin) {
        int pila[] = new int[fin - inicio + 1];
        int top = -1;
        pila[++top] = inicio;
        pila[++top] = fin;
        while (top >= 0) {
            fin = pila[top--];
            inicio = pila[top--];
            int p = Partition(arreglo, inicio, fin);
            if (p - 1 > inicio) {
                pila[++top] = inicio;
                pila[++top] = p - 1;
            }
            if (p + 1 < fin) {
                pila[++top] = p + 1;
                pila[++top] = fin;
            }
        }
        return arreglo;
    }

    public static void main(String[] args) {
        Helper helper = new Helper();
        QuickSort quickSort = new QuickSort();
        int[] numeros = helper.GenerarPeorCaso(3);
        long tiempoInicio = System.nanoTime();
        numeros = quickSort.Ejecutar(numeros, 0, numeros.length - 1);
        long tiempoFin = System.nanoTime();
        helper.CalcularTiempo(tiempoInicio, tiempoFin);
        System.out.println("Tamaño: " + numeros.length);
    }

}
