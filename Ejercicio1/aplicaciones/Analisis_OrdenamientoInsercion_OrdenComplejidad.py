# Importo la LDE para poder usar el m�todo de ordenamiento
from Ejercicio1.modulos.LDE import ListaDobleEnlazada

import random
import time
import matplotlib.pyplot as plt

# valores_n = [10**i for i in range(1,5)] # Si es m�s de 4 el final del rango, consume mucha memoria y tarda en compilar
valores_n = range(100, 1000, 100)
tiempo = []

for n in valores_n:
    
    lde = ListaDobleEnlazada()  # Inicializo una LDE
    
    # Genero datos al azar
    for _ in range(n):
        lde.agregar(random.randint(-100, 100))
        
    tic = time.perf_counter()
    lde.ordenar()
    toc = time.perf_counter()
    tiempo.append(toc-tic)

print("Tama�o de la Lista Doble Enlazada:", lde.tamanio)


'''Gr�fico para tama�o de lista = 1000'''

plt.clf()
plt.title('Tiempos en fn. del nro de elementos - Ordenamiento Por Inserci�n\n', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold'})

plt.plot(valores_n, tiempo, label="Ordenamiento por Inserci�n")
plt.legend()

plt.xlabel("tama�o (n)")
plt.xlim(0, 1000)

plt.ylabel("tiempo (s)")
# plt.yticks(range(0.000,0.310,0.050))

plt.show