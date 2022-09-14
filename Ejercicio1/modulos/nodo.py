class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None
        self.anterior = None
    
    @property
    def dato(self):
        return self._dato
    
    @dato.setter
    def dato(self,nuevoDato):
        self._dato = nuevoDato
    
    @property
    def anterior(self):
        return self._anterior
        
    @anterior.setter
    def anterior(self,nuevoAnterior):
        self._anterior = nuevoAnterior
    
    @property
    def siguiente(self):
        return self._siguiente
    
    @siguiente.setter
    def siguiente(self,nuevoSiguiente):
        self._siguiente = nuevoSiguiente