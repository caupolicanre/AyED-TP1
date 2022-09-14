from modulos.LDE import ListaDoble
from carta import Carta

class ColaDoble(ListaDoble):
    
    def encolar(self, item):
        ListaDoble.agregar(item)
        
    def desencolar(self):
        ListaDoble.extraer(ListaDoble.tamanio-1)

pruebaColaDoble= ColaDoble()
print(pruebaColaDoble.esta_vacia())