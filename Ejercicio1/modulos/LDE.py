
class Nodo:
    def __init__(self, datoInicial):
        '''
        Atributos del Nodo
        
        '''
        self._dato = datoInicial
        self._siguiente = None
        self._anterior = None
    
    def __str__(self):
        return str(self.dato)

    def __repr__(self):
        return str(self.dato)
    
    
    # Propiedades
    
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
    
    
    
    def __str__(self):
        '''Retorna una lista de los Nodos dentro 
        de la Lista Doble Enlazada'''
        
        return str([nodo.dato for nodo in self])
    
    def __getitem__(self, pos):
        nodo = self.cabeza
        
        for i,nodo in enumerate(self):
            nodo.siguiente
            if i == pos:
                break
    
    def __iter__(self):
        '''Método para iterar la lista'''
        
        nodo = self.cabeza

        while nodo:
            yield nodo
            nodo = nodo.siguiente
    
    def __add__(self):
        return self.concatenar()

        
    
    # Métodos / Funciones

    def esta_vacia(self):
        return self._tamanio == 0
    
    
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
        
        if posicion < 0 or posicion >= self._tamanio:
            raise IndexError()
        
        
        if posicion == 0:
            self.agregar(item)
            
        elif posicion == self._tamanio-1:
            self.anexar(item)
            
        else:
            nuevoNodo = Nodo(item)
            
            temp = self.cabeza
            
            for i in range(posicion-1): # Se pone posición-1 para que se inserte el item en el índice que ingresó el usuario
                temp = temp.siguiente
                
            siguienteTemp = temp.siguiente
            temp.siguiente = nuevoNodo
            nuevoNodo.siguiente = siguienteTemp
            
            self._tamanio+=1
            
            
    
    def extraer(self, posicion=-1):
        
        if posicion < -1 or posicion >= self._tamanio:
            raise IndexError
        
        if posicion==-1 or posicion==self.tamanio-1:
            temp = self.cola
            self.cola = temp.anterior
            
            self._tamanio-=1
            return temp
            
        elif posicion == 0:
            temp = self.cabeza
            self.cabeza = temp.siguiente
            
            self._tamanio-=1
            return temp
        
        else:
            temp = self.cabeza
            
            for i in range(posicion):
                temp = temp.siguiente
            
            temp.anterior.siguiente = temp.siguiente
            temp.anterior = temp.siguiente
            
            self._tamanio-=1
            return temp
        
    
    
    def concatenar(self, lista):
        temp = lista.cabeza
        
        for i in range(lista.tamanio):
            self.anexar(temp.dato)
            temp = temp.siguiente
     
        return self




# Pruebas locales

if __name__ == "__main__":

    # Inicializo 2 listas
    lista1=ListaDobleEnlazada()
    lista2=ListaDobleEnlazada()


    # Agrego 3 items al inicio de la 2da lista
    lista2.agregar(1)
    lista2.agregar(2)
    lista2.agregar(3)
    # Anexo 2 items al final de la 2da lista
    lista2.anexar(8)
    lista2.anexar(9)
    
    # Muestro la lista 2 antes y después de insertarle un elemento
    print(lista2)
    lista2.insertar(3, "Fito Paez") # Se inserta el item en el índice 3
    print(lista2)
    
    print("\nInserto al inicio de la lista 2:")
    lista2.insertar(0, "dou") # Se inserta en el item en la posición 3
    print(lista2)
    
    print("\nInserto al final de la lista 2:")
    lista2.insertar(lista2.tamanio-1, "uod") # Se inserta en el item en la posición 3
    print(lista2)



    #Muestro las 2 listas y pregunto si están vacías
    print("\nLista 1:", lista1)
    print("Lista 1 esta vacia:", lista1.esta_vacia())
    print("Tamaño de la Lista 1:", lista1.tamanio)
    
    print("\nLista 2:", lista2)
    print("Lista 2 está vacía:", lista2.esta_vacia())
    print("Tamaño de la Lista 2:", lista2.tamanio)
    
    
    # Pruebo el extraer en la lista 2
    print("\nExtraigo el primer elemento de la lista 2:", lista2.extraer(0))
    print("Lista 2:", lista2)
    
    print("\nExtraigo el último elemento de la lista 2:", lista2.extraer())
    print("Lista 2:", lista2)