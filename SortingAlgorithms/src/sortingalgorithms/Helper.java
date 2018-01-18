package sortingalgorithms;

import java.util.Arrays;
import java.util.Collections;

public class Helper {

    public void Imprimir(int[] numeros) {
        for (int i = 0; i < numeros.length; i++) {
            System.err.println(numeros[i]);
        }
    }

    public int[] GenerarPeorCaso(int cantidad) {
        int total = (int) Math.pow(10, cantidad);
        Integer[] array = new Integer[total];
        for (int i = 0; i < total; i++) {
            array[i] = (int) (Math.random() * total);
        }
        Arrays.sort(array, Collections.reverseOrder());
        int[] arreglo = Arrays.stream(array).mapToInt(Integer::intValue).toArray();
        return arreglo;
    }

    void CalcularTiempo(long tiempoInicio, long tiempoFin) {
        long tiempoTotal = tiempoFin - tiempoInicio;
        System.out.println("Tiempo total: " + tiempoTotal);
    }
}
