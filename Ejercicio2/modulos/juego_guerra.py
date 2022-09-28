from cola_doble import ColaDoble
from mazo import Mazo
import random as rd

class JuegoGuerra:

    def __init__(self, seed):
        # self.cantidad_turnos = cant_turnos 
        # self.turnos_jugados = 0
        # self.ganador = None
        # self.empate = None
        
        self.mazo_mesa = Mazo()
        self.mazo_jugador1 = Mazo()
        self.mazo_jugador2 = Mazo()
        
        self.semilla = seed
        
    
    # Propiedades

    @property
    def turnos_jugados(self):
        return self._turnos_jugados
    
    def crear_mazo(self):
        None

    def repartir(self):
        for i, carta in enumerate(self.mazo_mesa):
            if i%2 == 0:
                self.mazo_jugador1.agregar_carta(carta)
            if i%2 != 0:
                self.mazo_jugador2.agregar_carta(carta)
        return mazo1 y mazo2.
    def iniciar_juego(self):
        None
    
    def 