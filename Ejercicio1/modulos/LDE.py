
class Nodo:
    '''asd'''
    def __init__(self, datoInicial):
        self._dato = datoInicial
        self._siguiente = None
        self._anterior = None
    
    def __str__(self):
        return str(self.dato)

    def __repr__(self):
        return str(self)
    
    @property
    def dato(self):
        return self._dato
    
    @dato.setter
    def dato(self, nuevoDato):
        self._dato = nuevoDato
    
    @property
    def anterior(self):
        return self._anterior
        
    @anterior.setter
    def anterior(self, nuevoAnterior):
        self._anterior = nuevoAnterior
    
    @property
    def siguiente(self):
        return self._siguiente
    
    @siguiente.setter
    def siguiente(self, nuevoSiguiente):
        self._siguiente = nuevoSiguiente


class ListaDobleEnlazada:
    
    def __init__(self):
        '''Atributos de la Lista Doble Enlazada'''
        self.cabeza = None
        self.cola = None
        self._tamanio = 0   # Contador para el tamaño de la lista
    
    def __str__(self):
        #lista = [str(Nodo) for Nodo in self]    # Preguntar si se puede utilizar esta lista en el TP
        for Nodo in self:
            return str(Nodo)
        

    def __repr__(self):
        return str(self)
    
    def __iter__(self):
        nodo = self.cabeza

        while nodo:
            yield nodo
            nodo = nodo.siguiente
    
    def __add__(self):
        return self.concatenar()


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
        

    
    # Métodos / Funciones

    def esta_vacia(self):
        return self.tamanio == 0
    
    
    def agregar(self, item):
        nuevoNodo = Nodo(item)
        
        if self.esta_vacia():
            self.cabeza = nuevoNodo
            self.cola = nuevoNodo
        else:
            nuevoNodo.siguiente = self.cabeza   # Asigno al nuevo nodo el atributo de siguiente con el valor de la cabeza
            self.cabeza.anterior = nuevoNodo    # Asigno al nodo de la cabeza el atributo de anterior con el valor del nodo nuevo
            self.cabeza = nuevoNodo             # Actualizo la cabeza con el nodo nuevo
        
        self._tamanio+=1    # Sumamos 1 al contador del tamaño de la lista. IMPORTANTE: si actualizamos el contador al inicio de la función, no anda, hay que hacerlo al inicio
    
    def anexar(self, item):
        nuevoNodo = Nodo(item)
        
        if self.esta_vacia():
            self.cabeza = nuevoNodo
            self.cola = nuevoNodo
        else:
            nuevoNodo.anterior = self.cola
            self.cola.siguiente = nuevoNodo
            self.cola = nuevoNodo
            
        self._tamanio+=1


    def insertar(self, posicion, item):
        
        if posicion < 0 or posicion >= self.tamanio:
            raise IndexError()
        
        
        if posicion == 0:
            self.agregar(item)
            
        elif posicion == self.tamanio-1:
            self.anexar(item)
            
        else:
            nuevoNodo = Nodo(item)
            
            temp = self.cabeza
            
            for i in range(posicion):
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
    
    
    def concatenar(self, lista):
        temp = lista.cabeza
        
        for i in range(lista.tamanio):
            self.anexar(temp.dato)
            temp = temp.siguiente
     
        return self




# Pruebas
if __name__ == "__main__":

    lista1=ListaDobleEnlazada()
    lista2=ListaDobleEnlazada()

    lista2.agregar(1)
    lista2.agregar(2)
    lista2.agregar(3)

    lista2.anexar(8)
    lista2.anexar(9)

    print(lista1.esta_vacia())

    print(lista2)