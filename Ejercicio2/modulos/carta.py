from nodo import Nodo

class Carta(Nodo):
    
    def __init__(self, palo, numero):
        self._palo = palo
        self._numero = numero
        self.boca_abajo = None
        self.boca_arriba = None
    
    def __str__(self):
        return str(self._palo + " " + self._numero)
    
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