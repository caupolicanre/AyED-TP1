from cola_doble import ColaDoble

class Mazo:
    
    def __init__(self):
        self.mazo = ColaDoble()
    
    def __str__(self):
        return str(self.mazo)
    
    def __iter__(self):
        return iter(self.mazo)
    
    def agregar_carta(self, cartaNueva):
        self.mazo.agregarFinal(cartaNueva)

    def jugar_carta(self, estadoCara="Boca abajo"):
        cartaJugada = self.mazo.removerFinal()
        cartaJugada.estadoCara = estadoCara
        
        return cartaJugada
    
    def jugador_gana(self, cartasGanadas):
        self.mazo