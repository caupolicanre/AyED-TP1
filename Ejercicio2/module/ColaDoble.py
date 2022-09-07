from Ejercicio1.module.ListaDoble import Lista

class ColaDoble (Lista):
    
    def  encolar(self,item):
        Lista.agregar(item)
        
    def desencolar(self):
        Lista.extraer(Lista.tamanio-1)