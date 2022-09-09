
from cola_doble import ColaDoble

class JuegoGuerra:

    def __init__(self, random_seed, cant_turnos):
        self.cantidad_turnos = cant_turnos 
        self.turnos_jugados = 0
        self.ganador = None
        self.empate = None

        self.mazo_jugador1 = ColaDoble()
        self.mazo_jugador2 = ColaDoble()
        
    
    # Propiedades

    @property
    def turnos_jugados(self):
        return self._turnos_jugados
    


    def iniciar_juego(self):
        None