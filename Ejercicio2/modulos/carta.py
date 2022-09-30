class Carta:
    
    def __init__(self, palo, numero=0, jerarquia=0, cara="Boca abajo"):
        self._palo = palo
        self._numero = numero
        self._cara = cara
        self._jerarquia = jerarquia 
        
    
    def __str__(self):
        if self._cara == "Boca abajo":
            return "-X"
        else:
            return str(self._palo) + str(self._numero)


    # Propiedades
    
    @property
    def palo(self):
        return self._palo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def cara(self):
        return self._cara
    
    @cara.setter
    def cara(self, nuevaCara):
        self._cara = nuevaCara
        
    @property
    def jerarquia(self):
        return self._jerarquia
    


# Pruebas locales

if __name__ == "__main__":
    
    carta1 = Carta(palo="♥", numero=5, cara="Boca abajo")
    print(carta1)
    
    carta2 = Carta(palo="♠", numero=10, cara="Boca arriba")
    print(carta2)
