
from __future__ import annotations


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
        Atributos del Nodo.

        Parameters
        ----------
        datoInicial : any type
            Almacena el valor ingresado por el usuario. 
            Puede ser de cualquier tipo.
        
        Returns
        -------
        None.

        '''
        self._dato = datoInicial
        self._anterior = None
        self._siguiente = None
    
    
    # Métodos Mágicos
    
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
    
    # def __lt__(self, other: Nodo()):
    #     if self._dato < other._dato:
    #         True
    #     else:
    #         False
    
    # def __gt__(self, other: Nodo()):
    #     if self._dato > other._dato:
    #         True
    #     else:
    #         False

    # def __eq__(self, other: Nodo()):
    #     if self._dato == other._dato:
    #         True
    #     else:
    #         False
    
    def __getitem__(self, indice):
        return self.dato[indice]
    
    
    # Atributos
    
    @property
    def dato(self):
        '''
        Getter del dato que almacena el Nodo.

        Returns
        -------
        any type
            Retorna el dato del Nodo.

        '''
        return self._dato
    
    @dato.setter
    def dato(self, nuevoDato):
        '''
        Setter del dato que almacena el Nodo.

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
            Nueva referencia al Nodo que va a reemplazar 
            el anterior del Nodo actual.

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
            Nueva referencia al Nodo que va a reemplazar 
            el siguiente del Nodo actual.

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

        Atributos
        -------
        cabeza = reference
        cola = reference
        tamanio = int

        '''
        
        self.cabeza = None
        self.cola = None
        self._tamanio = 0   # Contador para el tamaño de la lista
    
    
    # Atributos
    
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
            Nueva referencia al Nodo que va a reemplazar la 
            cabeza actual de la Lista.

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
            Nueva referencia al Nodo que va a reemplazar la 
            cola actual de la Lista.

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
    
    
    # Métodos Mágicos
    
    def __str__(self):
        '''
        Lista de los Nodos dentro de la Lista Doble Enlazada.

        Returns
        -------
        string
            Retorna un string de una Lista de los Nodos de la LDE.

        '''
        return str([nodo.dato for nodo in self])
    
    def __iter__(self):
        '''
        Método para iterar la lista
        '''
        
        nodo = self.cabeza

        while nodo:
            yield nodo
            nodo = nodo.siguiente
    
    def __add__(self, lista):
        '''
        Cuando se sumen dos Listas con el operador "+",
        se llama al método "concatenar", para concatenarlas.

        Returns
        -------
        class
            Retorna la lista actual con la lista pasada como parámetro 
            concatenada al final de la primera.

        '''
        return self.concatenar(lista)
    
    # Métodos

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
        
        if self.tamanio == 0:       # Si la lista está vacía, se asigna como cabeza y cola el nuevo Nodo
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
        
        if self.tamanio == 0:
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
        
        
        if posicion < 0 or posicion >= self.tamanio:
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
            
        elif posicion == self.tamanio-1:
            '''
            El usuario ingresa la última posición.
            Se inserta el elemento en la última posición de la Lista.
            Quedando el Nodo insertado una posición antes de la cola.
            '''
            
            nuevoNodo = Nodo(item)
            
            # Queda el nuevo Nodo antes de la cola
            self.cola.anterior.siguiente = nuevoNodo
            nuevoNodo.anterior = self.cola.anterior
            nuevoNodo.siguiente = self.cola
            self.cola.anterior = nuevoNodo            
            
            self._tamanio+=1
            
        else:
            '''
            La posición ingresada por el usuario no es un extremo.
            Se recorre la lista hasta la posición recibida como parámetro,
            y se inserta el elemento recibido.
            '''
            
            nuevoNodo = Nodo(item)
            
            temp = self.cabeza  # El nodo inicial arranca en la cabeza y recorre la Lista hasta la posición recibida por el parámetro
            
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
        Si no se indica el parámetro "posicion", se elimina y devuelve 
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
        
        if posicion < -1 or posicion >= self.tamanio:
            '''
            El usuario ingresa una posición fuera del rango.
            '''
            raise IndexError
        
        if posicion == -1 or posicion == self.tamanio-1:
            '''
            El usuario no ingresa posición o ingresa la última posición.
            Se extrae el último elemento de la Lista.
            '''
            temp = self.cola            # Guardo en una variable auxiliar el Nodo extraido, para poder retornarlo
            aux = self.cola.anterior
            self.cola.anterior = None   # Elimino la referencia del Nodo a extraer
            self.cola = aux             # Actualizo la cola con el Nodo anterior
            
            self._tamanio-=1
            return temp
            
        elif posicion == 0:
            '''
            El usuario ingresa la primera posición.
            Se extrae el primer elemento de la Lista.
            '''
            temp = self.cabeza                      # Guardo en una variable auxiliar el Nodo extraido, para poder retornarlo
            self.cabeza.siguiente.anterior = None   # Elimino la referencia del Nodo a extraer
            self.cabeza = temp.siguiente            # Actualizo la cabeza con el Nodo siguiente
            
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
            
            nodoExtraer.anterior.siguiente = nodoExtraer.siguiente  # Elimino la referencia que tiene el Nodo anterior y la reemplazo por la referencia al Nodo siguiente del que se extrajo
            nodoExtraer.siguiente.anterior = nodoExtraer.anterior   # Elimino la referencia que tiene el Nodo siguiente y la reemplazo por la referencia al Nodo anterior del que se extrajo
            
            self._tamanio-=1
            return temp         # Retorno el Nodo extraido
        
        
    def copiar(self):
        '''
        Realiza una copia de la lista elemento a elemento
        y devuelve la copia.

        Returns
        -------
        nuevaLista : class
            Retorna una copia de la Lista Doble Enlazada.

        '''
        nuevaLista = ListaDobleEnlazada()
        temp = self.cabeza
        
        for i in range(self.tamanio):
            nuevaLista.anexar(temp.dato)
            temp = temp.siguiente
        
        return nuevaLista
    
    
    def invertir(self):
        '''
        Invierte el orden de los elementos de la lista.

        Returns
        -------
        class
            Retorna la Lista Doble Enlazada Invertida.

        '''
        
        # Actualizo la cabeza y cola de la Lista
        tempCabeza = self.cabeza
        self.cabeza = self.cola
        self.cola = tempCabeza
        
        # Invierto los enlaces de cada Nodo de la Lista
        for nodo in self:
            tempNodoAnterior = nodo.anterior
            nodo.anterior = nodo.siguiente
            nodo.siguiente = tempNodoAnterior

        
        return self
    
    
    def ordenar(self):
        '''
        Ordena los elementos de la lista de "menor a mayor".

        Returns
        -------
        None.

        '''
        
        terminar = None
        
        while self.cabeza != terminar:
            nodoActual = self.cabeza
            temp = self.cabeza
            
            while temp.siguiente != terminar:   # Cuando llegue a la cola, temp.siguiente == None, por ende va a salir del bucle
                cambiar = temp.siguiente        # Almaceno el Nodo siguiente a "temp" para poder compararlos
                
                if temp.dato > cambiar.dato:    # Si el Nodo de la izquierda (temp) es mayor al de la derecha (cambiar), desplaza hacia la derecha el primer Nodo (temp)
                    # Desplazamiento del Nodo mayor (temp)
                    
                    temp.siguiente = cambiar.siguiente
                    temp.anterior = cambiar
                    
                    cambiar.siguiente = temp
                    
                    if temp != self.cabeza:
                        nodoActual.siguiente = cambiar
                    else:                       # La primera vez del bucle entra a este else, y actualiza la cabeza con
                        self.cabeza = cambiar   # Actualizo la cabeza nueva
                    
                    aux = temp
                    temp = cambiar
                    cambiar = aux
                    
                    # Actualizo la cola nueva
                    self.cola = cambiar
                    
                
                nodoActual = temp
                temp = temp.siguiente
                       
                
            terminar = temp     # Actualizo la variable para terminar de ordenar
    
    
    def concatenar(self, lista):
        '''
        Recibe una lista como argumento y retorna la lista 
        actual con la lista pasada como parámetro concatenada 
        al final de la primera.
        Funciona si se utiliza el operador '+'

        Parameters
        ----------
        lista : class
            Recibe como parametro una Lista Doble Enlazada

        Returns
        -------
        class
            Retorna la Lista actual concatenada con la Lista
            recibida como parámetro.

        '''
        
        if self.tamanio == 0:
            '''
            La Lista actual está vacía.
            Retorna la Lista recibida como parámetro
            '''
            return lista
        
        elif lista.tamanio == 0:
            '''
            La Lista recibida como parámetro está vacía.
            Retorna la Lista actual.
            '''
            return self
        
        else:
            '''
            Ambas Listas contienen elementos.
            Retorna la Lista actual concatenada con la Lista
            recibida como parámetro.
            '''
            # Conecto la cola de la Lista actual, con la cabeza de la Lista recibida
            self.cola.siguiente = lista.cabeza
            lista.cabeza.anterior = self.cola
            self.cola = lista.cola
            self._tamanio = self._tamanio + lista._tamanio
            
            return self




# Pruebas locales. TODO FUNCIONA

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
    
    
    # =================
    # INSERTAR FUNCIONA
    # =================
    
    print("\n========")
    print("INSERTAR")
    print("========")
    
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
    
    print("\nInserto al final de la lista 2:")
    lista2.insertar(lista2.tamanio-1, 101) # Se inserta en el item en la posición 3
    print(lista2)
    print("Lista 2 Cola:", lista2.cola)
    

    # =================================
    # TODO EL EXTRAER FUNCIONA PERFECTO
    # =================================
    
    print("\n\n=======")
    print("EXTRAER")
    print("=======")
    
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
    
    
    # ===============
    # COPIAR FUNCIONA
    # ===============
    
    print("\n\n======")
    print("COPIAR")
    print("======")
    
    # Lista 2 Original
    print("\nLista 2 Original:\n", lista2)
    print("Lista 2 Copiada:\n", lista2.copiar())
    
    
    # =================
    # INVERTIR FUNCIONA
    # =================
    
    print("\n\n========")
    print("INVERTIR")
    print("========")
    
    print("\nLista 2 Original:\n", lista2)
    print("Lista 2 Invertida:\n", lista2.invertir())
    
    
    # =============
    # CONCATENAR
    # =============
    
    print("\n\n==========")
    print("CONCATENAR")
    print("==========")
    
    # Agrego algunos elementos a la lista 1 para poder concatenarla con la lista 2
    lista1.agregar(91)
    lista1.agregar(19)
    lista3=ListaDobleEnlazada()
    lista3.agregar(22)
    lista3.agregar(33)
    
    print("\nLista 1:", lista1)
    print("Lista 2:", lista2)
    print("\nLista concatenada:", lista2.concatenar(lista1))
    
    print("\nLista 1:", lista1)
    print("Lista 3:", lista3)
    print("\nLista concatenada:", lista1+lista3)
    
    
        # ========
    # GET ITEM
    # ========
    print("\n\n=======")
    print("GET ITEM")
    print("=======")
    
    print(f"\nLista 1: {lista1}\n")
    print("Lista1[0]:", lista1[0])
    print("Lista1[1]:", lista1[1])
    print("Lista1[2]:", lista1[2])
    
    
    # ========
    # ORDENAR
    # ========
    
    print("\n\n=======")
    print("ORDENAR")
    print("=======")
    
    lista4 = ListaDobleEnlazada()
    lista4.agregar(2)
    lista4.agregar(56)
    lista4.anexar(17)
    
    print("\nLista Original:\n", lista4)
    print("Cabeza original:", lista4.cabeza)
    print("Cola original:", lista4.cola)
    lista4.ordenar()
    print("\nLista ordenada de menor a mayor:\n", lista4)
    print("Cabeza nueva:", lista4.cabeza)
    print("Cola nueva:", lista4.cola)
    