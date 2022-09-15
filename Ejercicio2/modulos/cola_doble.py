from modulos.LDE import ListaDobleEnlazada
from carta import Carta

class ColaDoble(ListaDobleEnlazada):
    
    def encolar(self, item):
        ListaDobleEnlazada.agregar(item)
        
    def desencolar(self):
        ListaDobleEnlazada.extraer(ListaDobleEnlazada.tamanio-1)

pruebaColaDoble= ColaDoble()
print(pruebaColaDoble.esta_vacia())