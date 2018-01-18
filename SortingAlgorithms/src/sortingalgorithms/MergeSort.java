/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sortingalgorithms;

/**
 *
 * @author William
 */
public class MergeSort {

    void Merge(int arreglo[], int izquierda, int medio, int derecha) {
        int n1 = medio - izquierda + 1;
        int n2 = derecha - medio;
        int arregloIzquierda[] = new int[n1];
        int arregloDerecha[] = new int[n2];
        for (int i = 0; i < n1; ++i) {
            arregloIzquierda[i] = arreglo[izquierda + i];
        }
        for (int j = 0; j < n2; ++j) {
            arregloDerecha[j] = arreglo[medio + 1 + j];
        }
        int i = 0, j = 0;
        int k = izquierda;
        while (i < n1 && j < n2) {
            if (arregloIzquierda[i] <= arregloDerecha[j]) {
                arreglo[k] = arregloIzquierda[i];
                i++;
            } else {
                arreglo[k] = arregloDerecha[j];
                j++;
            }
            k++;
        }
        while (i < n1) {
            arreglo[k] = arregloIzquierda[i];
            i++;
            k++;
        }
        while (j < n2) {
            arreglo[k] = arregloDerecha[j];
            j++;
            k++;
        }
    }

    int[] Ejecutar(int arreglo[], int izquierda, int derecha) {
        if (izquierda < derecha) {
            int medio = (izquierda + derecha) / 2;
            Ejecutar(arreglo, izquierda, medio);
            Ejecutar(arreglo, medio + 1, derecha);
            Merge(arreglo, izquierda, medio, derecha);
        }
        return arreglo;
    }

    public static void main(String[] args) {
        Helper helper = new Helper();
        MergeSort mergeSort = new MergeSort();
        int[] numeros = helper.GenerarPeorCaso(7);
        long tiempoInicio = System.nanoTime();
        numeros = mergeSort.Ejecutar(numeros, 0, numeros.length - 1);
        long tiempoFin = System.nanoTime();
        helper.CalcularTiempo(tiempoInicio, tiempoFin);
        System.out.println("Tamaño: " + numeros.length);
    }

}
