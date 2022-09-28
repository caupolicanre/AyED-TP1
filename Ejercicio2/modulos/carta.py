class Carta:
    
    def __init__(self, palo, numero=0, jerarquia=0, cara="boca abajo"):
        self._palo = palo
        self._numero = numero
        self._cara = cara
        self._jerarquia = jerarquia 
        
    
    def __str__(self):
        if self._cara == "boca abajo":
            return "-X"
        else:
            return str(self._palo) + " " + str(self._numero)


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
    
    @property
    def cara(self):
        return self._cara
    
    @cara.setter
    def cara(self, nuevaCara):
        self._cara = nuevaCara
    

        
if __name__ == "__main__":
    pruebaCarta=Carta(palo="corazon", numero=5,cara="boca abajo")
    print(pruebaCarta)
    
