from LDE import Nodo

class Carta(Nodo):
    
    def __init__(self, palo, numero, cara = "boca abajo"):
        self._palo = palo
        self._numero = numero
        self._cara = cara
        
    
    def __str__(self):
        if self._cara == "boca abajo":
            return "-X"
        elif self._cara=="boca arriba":
            return str(self._palo+" "+str(self._numero))
    
    def __repr__(self):
        return str(self)

    # Propiedades
    
    @property
    def palo(self):
        return self._palo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def boca_abajo(self):
        return self.boca_abajo
    
    @boca_abajo.setter
    def boca_abajo(self, estado):
        self.boca_abajo = estado

    @property
    def boca_arriba(self):
        return self.boca_arriba
    
    @boca_arriba.setter
    def boca_arriba(self, estado):
        self.boca_arriba = estado
    

        
if __name__ == "__main__":
    pruebaCarta=Carta(palo="corazon", numero=5,cara="boca abajo")
    print(pruebaCarta)
    
