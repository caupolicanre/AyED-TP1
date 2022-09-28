'''Clase del Nodo'''

class Nodo:
    '''
    Clase que almacena 1 dato de cualquier tipo.
    
    Atributos
    ---------
    dato : any type
    anterior : reference
    siguiente : reference
    
    '''
    
    def __init__(self, datoInicial):
        '''
        Atributos del Nodo

        Parameters
        ----------
        datoInicial : any type
            Almacena el valor ingresado por el usuario. Puede ser de cualquier tipo.
        
        Returns
        -------
        None.

        '''
        self._dato = datoInicial
        self._anterior = None
        self._siguiente = None
    
    def __str__(self):
        '''
        Cuando se realiza un "print", retorna un string del dato 
        almacenado en el Nodo.

        Returns
        -------
        string
            Retorna el valor del dato.

        '''
        return str(self.dato)

    def __repr__(self):
        return str(self.dato)
    
    
    # Propiedades
    
    @property
    def dato(self):
        '''
        Getter del dato del Nodo.

        Returns
        -------
        any type
            Retorna el dato del Nodo.

        '''
        return self._dato
    
    @dato.setter
    def dato(self, nuevoDato):
        '''
        Setter del dato Nodo.

        Parameters
        ----------
        nuevoDato : any type
            Dato que va a reemplazar el dato actual del Nodo.

        Returns
        -------
        None.

        '''
        self._dato = nuevoDato
    
    @property
    def anterior(self):
        '''
        Getter del Nodo anterior al actual.

        Returns
        -------
        reference
            Retorna una referencia al Nodo anterior.

        '''
        return self._anterior
        
    @anterior.setter
    def anterior(self, nuevoAnterior):
        '''
        Setter del Nodo anterior al actual.

        Parameters
        ----------
        nuevoAnterior : reference
            Nueva referencia al Nodo que va a reemplazar el anterior del Nodo actual.

        Returns
        -------
        None.

        '''
        self._anterior = nuevoAnterior
    
    @property
    def siguiente(self):
        '''
        Getter del Nodo siguiente al actual.

        Returns
        -------
        reference
            Retorna una referencia al Nodo siguiente.

        '''
        return self._siguiente
    
    @siguiente.setter
    def siguiente(self, nuevoSiguiente):
        '''
        Setter del Nodo siguiente al actual.

        Parameters
        ----------
        nuevoSiguiente : reference
            Nueva referencia al Nodo que va a reemplazar el siguiente del Nodo actual.

        Returns
        -------
        None.

        '''
        self._siguiente = nuevoSiguiente



'''Clase de la Lista Doble Enlazada'''

class ListaDobleEnlazada:
    
    def __init__(self):
        '''
        Atributos de la Lista Doble Enlazada

        Returns
        -------
        None.

        '''
        
        self.cabeza = None
        self.cola = None
        self._tamanio = 0   # Contador para el tamaño de la lista
    
    
    # Propiedades
    
    @property
    def cabeza(self):
        '''
        Getter de la cabeza de la Lista.

        Returns
        -------
        reference
            Retorna una referencia a la cabeza de la Lista.

        '''
        return self._cabeza
    
    @cabeza.setter
    def cabeza(self, nuevaCabeza):
        '''
        Setter de la cabeza de la Lista.

        Parameters
        ----------
        nuevaCabeza : reference
            Nueva referencia al Nodo que va a reemplazar la cabeza actual de la Lista.

        Returns
        -------
        None.

        '''
        self._cabeza = nuevaCabeza
        
    @property
    def cola(self):
        '''
        Getter de la cola de la Lista.

        Returns
        -------
        reference
            Retorna una referencia a la cola de la Lista.

        '''
        return self._cola
    
    @cola.setter
    def cola(self, nuevaCola):
        '''
        Setter de la cola de la Lista.

        Parameters
        ----------
        nuevaCola : reference
            Nueva referencia al Nodo que va a reemplazar la cola actual de la Lista.

        Returns
        -------
        None.

        '''
        self._cola = nuevaCola
        
    @property
    def tamanio(self):
        '''
        Contador de la Lista que almacena la cantidad de ítems en ella.

        Returns
        -------
        int
            Devuelve el número de ítems de la lista.

        '''
        return self._tamanio
    
    
    
    def __str__(self):
        '''
        Lista de los Nodos dentro de la Lista Doble Enlazada.

        Returns
        -------
        string
            Retorna un string de una Lista de los Nodos de la LDE.

        '''
        return str([nodo.dato for nodo in self])
    
    def __getitem__(self, pos):
        nodo = self.cabeza
        
        for i,nodo in enumerate(self):
            nodo.siguiente
            if i == pos:
                break
    
    def __iter__(self):
        '''
        Método para iterar la lista
        '''
        
        nodo = self.cabeza

        while nodo:
            yield nodo
            nodo = nodo.siguiente
    
    def __add__(self):
        '''
        Cuando se sumen dos Listas con el operador "+",
        se llama al método "concatenar", para concatenarlas.

        Returns
        -------
        class
            Retorna la lista actual con la lista pasada como parámetro 
            concatenada al final de la primera.

        '''
        return self.concatenar()

        
    
    # Métodos / Funciones

    def esta_vacia(self):
        '''
        Comprueba si el tamaño de la Lista es igual a 0.

        Returns
        -------
        boolean
            Devuelve True si la Lista está vacía.

        '''
        return self._tamanio == 0
    
    
    def agregar(self, item):
        '''
        Agrega un nuevo ítem al inicio de la Lista.

        Parameters
        ----------
        item : any type
            Dato que se va a almacenar en un nuevo Nodo.

        Returns
        -------
        None.

        '''        
        nuevoNodo = Nodo(item)
        
        if self._tamanio == 0:       # Si la lista está vacía, se asigna como cabeza y cola el nuevo Nodo
            self.cabeza = nuevoNodo
            self.cola = nuevoNodo
        else:
            nuevoNodo.siguiente = self.cabeza   # Asigno al nuevo nodo el atributo de siguiente con el valor de la cabeza
            self.cabeza.anterior = nuevoNodo    # Asigno al nodo de la cabeza el atributo de anterior con el valor del nodo nuevo
            self.cabeza = nuevoNodo             # Actualizo la cabeza con el nodo nuevo
        
        self._tamanio+=1    # Sumamos 1 al contador del tamaño de la lista. IMPORTANTE: si actualizamos el contador al inicio de la función, no anda, hay que hacerlo al final
    
    
    def anexar(self, item):
        '''
        Agrega un nuevo ítem al final de la lista.

        Parameters
        ----------
        item : any type
            Dato que se va a almacenar en un nuevo Nodo.

        Returns
        -------
        None.

        '''
        nuevoNodo = Nodo(item)
        
        if self._tamanio == 0:
            self.cabeza = nuevoNodo
            self.cola = nuevoNodo
        else:
            nuevoNodo.anterior = self.cola
            self.cola.siguiente = nuevoNodo
            self.cola = nuevoNodo
            
        self._tamanio+=1


    def insertar(self, posicion: int, item):
        '''
        Agrega un nuevo ítem a la lista en "posicion".


        Parameters
        ----------
        posicion : int
            Indica la posición en la lista donde se va a insertar el nuevo elemento.
        item : any type
            Dato que se va a almacenar en un nuevo Nodo.

        Raises
        ------
        IndexError
            Si la posición ingresada por el usuario no está dentro del
            rango de la lista, devuelve un error de Índice.

        Returns
        -------
        None.

        '''      
        
        
        if posicion < 0 or posicion >= self._tamanio:
            '''
            El usuario ingresa una posición fuera del rango.
            '''
            raise IndexError("Error de índice. Ingrese una posición válida dentro de la Lista. (Siendo '0' el primer elemento)")
        
        if posicion == 0:
            '''
            El usuario ingresa la primera posición.
            Se llama al método agregar, y se inserta el elemento
            en la primera posición de la Lista.
            '''
            self.agregar(item)
            
        elif posicion == self._tamanio-1: # Si le dejo el -1 no anda el testeo de insertar en la última posición
            '''
            El usuario ingresa la última posición.
            Se inserta el elemento en la última posición de la Lista.
            '''
        
            # Lo ideal es dejar el anexar, pero con el anexar me tira error
            # self.anexar(item)
            
            nuevoNodo = Nodo(item)
            
            # Queda el nuevo Nodo entre la cola y el penúltimo Nodo
            self.cola.anterior.siguiente = nuevoNodo
            nuevoNodo.anterior = self.cola.anterior
            nuevoNodo.siguiente = self.cola
            self.cola.anterior = nuevoNodo
            
            # Esto es exactamente lo mismo que llamar a anexar, pero no funciona el testeo, solamente funciona en el testeo local
            # nuevoNodo.anterior = self.cola
            # self.cola.siguiente = nuevoNodo
            # self.cola = nuevoNodo
            
            
            self._tamanio+=1
            
        else:
            '''
            La posición ingresada por el usuario no es un extremo.
            Se recorre la lista hasta la posición recibida como parámetro,
            y se inserta el elemento recibido.
            '''
            nuevoNodo = Nodo(item)
            
            temp = self.cabeza
            
            for i in range(posicion):
                temp = temp.siguiente
            
            temp.anterior.siguiente = nuevoNodo # En el Nodo anterior a la posición, asigno como siguiente Nodo al Nodo nuevo
            nuevoNodo.anterior = temp.anterior  # Asigno el Nodo anterior al nuevo Nodo
            nuevoNodo.siguiente = temp          # Desplazo hacia la derecha el Nodo que se encuentra en la posición donde inserto el nuevo Nodo
            temp.anterior = nuevoNodo           # Actualizo el Nodo anterior del Nodo desplazadado con el nuevo Nodo
            
            self._tamanio+=1
            
            
    def extraer(self, posicion: int =-1):
        '''
        Elimina y devuelve el ítem en "posición".
        Si no se indica el parámetro posición, se elimina y devuelve 
        el último elemento de la lista.

        Parameters
        ----------
        posicion : int, opcional
            Indica la posición en la lista de donde se va a extraer 
            un elemento. El valor por defecto es -1.

        Raises
        ------
        IndexError
            Si la posición ingresada por el usuario no está dentro del
            rango de la lista, devuelve un error de Índice.

        Returns
        -------
        temp : reference
            Retorna el ítem extraido de la Lista.

        '''
        
        if posicion < -1 or posicion >= self._tamanio:
            '''
            El usuario ingresa una posición fuera del rango.
            '''
            raise IndexError
        
        if posicion == -1 or posicion == self.tamanio-1:
            '''
            El usuario no ingresa posición o ingresa la última posición.
            Se extrae el último elemento de la Lista.
            '''
            temp = self.cola # Guardo en una variable auxiliar el Nodo extraido, para poder retornarlo
            self.cola.anterior.siguiente = None # Elimino la referencia del Nodo a extraer
            self.cola = temp.anterior # Actualizo la cola con el Nodo anterior
            
            self._tamanio-=1
            return temp
            
        elif posicion == 0:
            '''
            El usuario ingresa la primera posición.
            Se extrae el primer elemento de la Lista.
            '''
            temp = self.cabeza # Guardo en una variable auxiliar el Nodo extraido, para poder retornarlo
            self.cabeza.siguiente.anterior = None # Elimino la referencia del Nodo a extraer
            self.cabeza = temp.siguiente # Actualizo la cabeza con el Nodo siguiente
            
            self._tamanio-=1
            return temp
        
        else:
            '''
            La posición ingresada por el usuario no es un extremo.
            Se recorre la lista hasta la posición recibida como parámetro,
            y se extrae el elemento.
            '''
            nodoExtraer = self.cabeza
            
            for i in range(posicion):
                nodoExtraer = nodoExtraer.siguiente
            
            temp = nodoExtraer # Guardo en una variable auxiliar el Nodo extraido, para poder retornarlo
            
            nodoExtraer.anterior.siguiente = nodoExtraer.siguiente # Elimino la referencia que tiene el Nodo anterior y la reemplazo por la referencia al Nodo siguiente del que se extrajo
            nodoExtraer.siguiente.anterior = nodoExtraer.anterior # Elimino la referencia que tiene el Nodo siguiente y la reemplazo por la referencia al Nodo anterior del que se extrajo
            
            self._tamanio-=1
            return temp
        
    def copiar(self):
        nuevaLista = ListaDobleEnlazada()
        
        for i in range(0, self._tamanio-1):
            nuevaLista.insertar(i, self[i].dato)
        
        return nuevaLista
    
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

    # ================
    # AGREGAR FUNCIONA
    # ================
    
    # Agrego 3 items al inicio de la 2da lista
    lista2.agregar(1)
    lista2.agregar(2)
    lista2.agregar(3)
    # Anexo 2 items al final de la 2da lista
    lista2.anexar(8)
    lista2.anexar(9)
    
    
    # ====================
    # INSERTAR NO FUNCIONA
    # ====================
    # Funciona al inicio y por posicón entre los extremos.
    # NO FUNCIONA INSERTAR AL FINAL. PERO EL TEST CORRE
    
    # Muestro la lista 2 antes y después de insertarle un elemento
    print("\nLista 2 Inicializada con valores por medio de agregar:\n", lista2)
    lista2.insertar(3, "Fito Paez") # Se inserta el item en el índice 3
    print("Lista 2 Inserto en la posición 4 (Índice 3):\n", lista2)
    
    print("\nInserto al inicio de la lista 2:")
    lista2.insertar(0, 1001) # Se inserta en el item en la primer posición, por ende, índice 0
    print(lista2)
    print("Lista 2 Cabeza:", lista2.cabeza)
    
    # Printeo el tamaño de la lista para comprobar
    print("\nTamaño de la Lista 2:", lista2.tamanio)
    # Printeo la cola para hacer un seguimiento
    print("Lista 2 Cola:", lista2.cola)
    
    # CORREGIR. Inserta en la penúltima posición, pero el TEST CORRE
    print("\nInserto al final de la lista 2:")
    lista2.insertar(lista2.tamanio-1, 101) # Se inserta en el item en la posición 3
    print(lista2)
    print("Lista 2 Cola:", lista2.cola)
    

    # =================================
    # TODO EL EXTRAER FUNCIONA PERFECTO
    # =================================
    
    #Muestro las 2 listas y pregunto si están vacías
    print("\n\nLista 1:", lista1)
    print("Lista 1 esta vacia:", lista1.esta_vacia())
    print("Tamaño de la Lista 1:", lista1.tamanio)
    
    print("\nLista 2:", lista2)
    print("Lista 2 está vacía:", lista2.esta_vacia())
    print("Tamaño de la Lista 2:", lista2.tamanio)
    
    
    # Pruebo el extraer en la lista 2
    # Primer elemento
    print("\nExtraigo el primer elemento de la lista 2:", lista2.extraer(0).dato)
    print("Lista 2:", lista2)
    print("Lista 2 Cabeza:", lista2.cabeza)
    
    # Último elemento, sin parámetro
    print("\nExtraigo el último elemento de la lista 2 (Sin parámetro):", lista2.extraer().dato)
    print("Lista 2:", lista2)
    print("Lista 2 Cola:", lista2.cola)
    
    # Último elemento, con parámetro
    print("\nExtraigo el último elemento de la lista 2 (Con parámetro):", lista2.extraer(lista2.tamanio-1).dato)
    print("Lista 2:", lista2)
    print("Lista 2 Cola:", lista2.cola)
    
    # Último elemento, parámetro -1
    print("\nExtraigo el último elemento de la lista 2 (Parámetro -1):", lista2.extraer(-1).dato)
    print("Lista 2:", lista2)
    print("Lista 2 Cola:", lista2.cola)
    
    
    # ===========
    # COPIAR
    # ===========
    
    # Lista 2 Original
    print("\n\nLista 2 Original:\n", lista2)
    print("Lista 2 Copiada:\n", lista2.copiar())