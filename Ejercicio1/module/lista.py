from module.nodo import Nodo

class Lista:
    
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
    
    
    # Propiedades
    
    @property
    def cabeza(self):
        return self._cabeza
    
    @cabeza.setter
    def cabeza(self, nuevaCabeza):
        self._cabeza = nuevaCabeza
        
    @property
    def cola(self):
        return self._cola
    
    @cola.setter
    def cola(self, nuevaCola):
        self._cola = nuevaCola
        
    @property
    def tamanio(self):
        return self._tamanio
        
    
    
    def esta_vacia(self):
        return self.tamanio == 0
    
    def agregar(self, item):
        temp = Nodo(item)
        
        if self.esta_vacia():
            self.cabeza = temp
            self.cola = temp
        else:
            temp.siguiente = self.cabeza   # Asigno al nuevo nodo el atributo de siguiente con el valor de la cabeza
            self.cabeza.anterior = temp    # Asigno al nodo de la cabeza el atributo de anterior con el valor del nodo nuevo
            self.cabeza = temp             # Actualizo la cabeza con el nodo nuevo
    
    def anexar(self, item):
        temp = Nodo(item)
        
        if self.esta_vacia():
            self.cabeza = temp
            self.cola = temp
        else:
            temp.anterior = self.cola
            self.cola.siguiente = temp
            self.cola = temp

    def insertar(self, posicion, item):
        
        if posicion < 0 or posicion > self.tamanio:
            raise IndexError()
        
        
        if posicion == 0:
            self.agregar(item)
            
        elif posicion == self.tamanio:
            self.anexar(item)
        
        