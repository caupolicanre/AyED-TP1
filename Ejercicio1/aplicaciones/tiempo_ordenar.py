# Importo la LDE para poder usar el método de ordenamiento
from modulos.LDE import ListaDobleEnlazada

import random
import time
import matplotlib.pyplot as plt

valores_n = [10**i for i in range(1,7)]
tiempo = []

for n in valores_n:
    
    lde = ListaDobleEnlazada()  # Inicializo una LDE
    
    # Genero datos al azar
    for i in valores_n:
        lde.agregar(random.randint(-100, 100))
        
    tic = time.perf_counter()
    lde.ordenar()
    toc = time.perf_counter()
    tiempo.append(toc-tic)



plt.clf()
plt.plot(valores_n, tiempo, label="Ordenamiento por Inserción")
#plt.yscale('log')
plt.xlabel("tama�o de la lista")
plt.ylabel("tiempos del algoritmo")
plt.title("Tiempos en fn. del nro de elementos")
plt.legend()
plt.show