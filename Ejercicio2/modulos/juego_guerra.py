from mazo import Mazo
from carta import Carta

import random as rd

class JuegoGuerra:

    def __init__(self, random_seed=22):
        
        self.mazo = Mazo()
        self.mazo_jugador1 = Mazo()
        self.mazo_jugador2 = Mazo()
        self.n_jugadores = 2
        self.valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.palos = ['♠', '♥', '♦', '♣']
        self._semilla = random_seed
        
        self.cantidad_turnos = None
        self.turnos_jugados = 0
        self.empate = False
        
        self.ganador = None
        
    
    # Propiedades

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

        cartas = []     # Lista para guardar las cartas, mezclarlas y luego crear un mazo
        jerarquia = 0   # Utilizo una jerarquía para comparar luego las cartas
        
        # Asigno cada número a los 4 palos
        for numero in self.valores:
            jerarquia+=1    # Aumento la jerarquía por cada iteración
            
            for palo in self.palos:
                carta = Carta(palo, numero, jerarquia, "Boca abajo")  # Creo una carta y le paso los parámetros correspondientes
                cartas.append(carta)    # Agrego la carta a la lista de cartas para crear luego el mazo
        
        rd.seed(self._semilla)   # Asigno una semilla para que se mezcle de una forma en específico
        rd.shuffle(cartas)      # Mezclo las cartas
        
        # Una vez mezcladas las cartas, las agrego al mazo
        for carta in cartas:
            self.mazo.agregar_carta(carta)


    def repartir(self):
        '''
        Reparte las cartas del mazo principal entre los
        mazos de los 2 jugadores.

        Returns
        -------
        None.

        '''
        
        nCartas = self.mazo.tamanio()
        print(nCartas)
        
        for i in range(nCartas):
            '''
            Si "i" es par, la carta va al mazo del Jugador 1,
            si es impar, la carta va al mazo del Jugador 2.
            '''
            if i%2 == 0:
                '''
                Reparte carta al Jugador 1.
                '''
                self.mazo_jugador1.agregar_carta(self.mazo.sacar_carta())
                
                
            if i%2 != 0:
                '''
                Reparte carta al Jugador 2.
                '''
                self.mazo_jugador2.agregar_carta(self.mazo.sacar_carta())
                
                
    
    
    def iniciar_juego(self):
        
        self.cantidad_turnos = 1000
        
        '''Se crea el mazo y se mezclan las cartas'''
        self.crear_mazo()
        
        '''Se reparten las cartas a cada jugador'''
        self.repartir()
        
        print(self.mazo_jugador1)
        print(self.mazo_jugador2)
        
        # while self.turnos_jugados < self.cantidad_turnos:
        #     try:
        #         self.mostrar_juego()
        #         self.turnos_jugados += 1
            
        #     except(ValueError):
        #         pass
            
        #     if len(self.mazo_jugador1) == 0:
        #         self.ganador = "Jugador 2"
        #         print("Gana Jugador 2")
        #         break
            
        #     elif len(self.mazo_jugador2) == 0:
        #         self.ganador = "Jugador 1"
        #         print("Gana Jugador 1")
        #         break
            
        #     elif self.turnos_jugados == self.cantidad_turnos:
        #         self.empate = True
        #         print("Empate")
        #         break


# Pruebas locales

if __name__ == "__main__":
    
    juego1 = JuegoGuerra()
    
    juego1.crear_mazo()
    juego1.repartir()
    
    print("\nMazo:\n", juego1.mazo)
    
    print("\nMazo Jugador 1:\n", juego1.mazo_jugador1)
    print("\nMazo Jugador 2:\n", juego1.mazo_jugador2)
    