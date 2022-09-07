from Ejercicio1.module.Nodo import Nodo

class Lista:
    
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self._tamanio = 0
    
    
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
        self._tamanio+=1
        
        if self.esta_vacia():
            self.cabeza = temp
            self.cola = temp
        else:
            temp.siguiente = self.cabeza   # Asigno al nuevo nodo el atributo de siguiente con el valor de la cabeza
            self.cabeza.anterior = temp    # Asigno al nodo de la cabeza el atributo de anterior con el valor del nodo nuevo
            self.cabeza = temp             # Actualizo la cabeza con el nodo nuevo
    
    
    def anexar(self, item):
        temp = Nodo(item)
        self._tamanio+=1
        
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
            
        else:
            nuevoNodo = Nodo(item)
            
            temp = self.cabeza
            
            for i in range(0,posicion-1):
                temp = temp.siguiente
                
            siguienteTemp = temp.siguiente
            temp.siguiente = nuevoNodo
            nuevoNodo.siguiente = siguienteTemp
            
            
    
    def extraer(self, posicion=-1):
        if posicion==-1 or posicion==self.tamanio:
            temp = self.cola
            self.cola = self.cola.anterior
            return temp
            
        elif posicion == 0:
            temp = self.cabeza
            self.cabeza = self.cabeza.siguiente
            return temp
        
        else:
            temp = self.cabeza
            
            for i in range(0,posicion):
                temp= temp.siguiente
            
            anteriorTemp = temp.anterior
            siguienteTemp= temp.siguiente
            
            anteriorTemp.siguiente = siguienteTemp
            siguienteTemp.anterior = anteriorTemp
             
            return temp