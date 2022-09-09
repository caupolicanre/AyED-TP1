from ListaDoble import Lista

class Pila(Lista):
    
    def apilar(self,item):
        Lista.agregar(item)
        
    def desapilar(self):
        Lista.extraer(0)