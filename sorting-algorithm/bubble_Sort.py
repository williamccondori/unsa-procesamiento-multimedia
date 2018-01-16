from time import time
import random
import math

def bubbleSort(numeros):
    desordenado = True
    n = len(numeros)
    for j in range(0, n):
        if desordenado:
            desordenado = False
            for i in range(0, n - 1 - j):
                if numeros[i] > numeros[i + 1]:
                    numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]
                    desordenado = True
        print(j)

def obtener_peor_caso(numero):
    lista = []
    datos = int(math.pow(10, numero))
    for i in range(0,datos):
        lista.append(random.randint(0, datos))
    lista.sort(reverse=True)
    return lista



lista = obtener_peor_caso(6)
print(lista)

t0 = time()
bubbleSort(lista)
t1 = time()

print("Tiempo: {0:f} segundos".format(t1 - t0))

print("Lista ordenada:")
print(lista, "\n")
