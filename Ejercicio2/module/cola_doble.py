from lista_doble import ListaDoble

class ColaDoble(ListaDoble):
    
    def encolar(self, item):
        ListaDoble.agregar(item)
        
    def desencolar(self):
        ListaDoble.extraer(ListaDoble.tamanio-1)