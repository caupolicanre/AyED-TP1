from mazo import Mazo
from carta import Carta

import random as rd

class JuegoGuerra:

    def __init__(self, seed):
        # self.cantidad_turnos = cant_turnos 
        # self.turnos_jugados = 0
        # self.ganador = None
        # self.empate = None
        
        self.mazo = Mazo()
        self.mazo_jugador1 = Mazo()
        self.mazo_jugador2 = Mazo()
        
        self._semilla = seed
        
    
    # Propiedades

    @property
    def semilla(self):
        '''
        Getter de semilla.

        Returns
        -------
        int
            Retorna la semilla con la que se inicializó el mazo.

        '''
        return self._semilla

    # @property
    # def turnos_jugados(self):
    #     return self._turnos_jugados
    
    
    
    def crear_mazo(self):
        '''
        Creo las cartas con su número, palo y jerarquía,
        luego las mezclo y agrego al mazo.

        Returns
        -------
        class
            Retorna el mazo creado.
            El mazo está hecho con una Cola Doble.

        '''
        
        valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        palos = ['♠', '♥', '♦', '♣']
        cartas = []     # Lista para guardar las cartas, mezclarlas y luego crear un mazo
        jerarquia = 0   # Utilizo una jerarquía para comparar luego las cartas
        
        # Asigno cada número a los 4 palos
        for numero in valores:
            jerarquia+=1    # Aumento la jerarquía por cada iteración
            
            for palo in palos:
                carta = Carta(palo, numero, jerarquia, "Boca abajo")  # Creo una carta y le paso los parámetros correspondientes
                cartas.append(carta)    # Agrego la carta a la lista de cartas para crear luego el mazo
        
        rd.seed(self.semilla)   # Asigno una semilla para que se mezcle de una forma en específico
        rd.shuffle(cartas)      # Mezclo las cartas
        
        # Una vez mezcladas las cartas, las agrego al mazo
        for carta in cartas:
            self.mazo.agregar_carta(carta)
        
        return self.mazo


    def repartir(self):
        '''
        Reparte las cartas del mazo principal entre los
        mazos de los 2 jugadores.

        Returns
        -------
        class
            Retorna mazo del Jugador 1.
            Creado con una Cola Doble.
        class
            Retorna mazo del Jugador 2.
            Creado con una Cola Doble.

        '''
        
        for i, carta in enumerate(self.mazo):
            '''
            Si "i" es par, la carta va al mazo del Jugador 1,
            si es impar, la carta va al mazo del Jugador 2.
            '''
            if i%2 == 0:
                self.mazo_jugador1.agregar_carta(carta)
                
            if i%2 != 0:
                self.mazo_jugador2.agregar_carta(carta)
                
        return self.mazo_jugador1, self.mazo_jugador2
    
    
    def iniciar_juego(self):
        None
    


# Pruebas locales

if __name__ == "__main__":
    
    juego1 = JuegoGuerra(22)
    
    print(juego1.crear_mazo())
    juego1.repartir()
    
    print("\nMazo:\n", juego1.mazo)
    
    print("\nMazo Jugador 1:\n", juego1.mazo_jugador1)
    print("\nMazo Jugador 2:\n", juego1.mazo_jugador2)
    