from mazo import Mazo, Carta

import random as rd

class JuegoGuerra:

    def __init__(self, random_seed=22):
        
        self.mazo = Mazo()
        self.mazo_jugador1 = Mazo()
        self.mazo_jugador2 = Mazo()
        self.cartas_mesa = []
        
        self.valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.palos = ['♠', '♥', '♦', '♣']
        
        self._semilla = random_seed
        
        self.cantidad_turnos = 10000    # Límite de turnos
        self.turnos = 0                 # Turnos jugados
        self.juego_empatado = False
        
        self.jugador_ganador = None
        
        
    
    # Propiedades

    @property
    def turnos_jugados(self) -> int:
        '''
        

        Returns
        -------
        int
            Cantidad de turnos jugados.

        '''
        return self.turnos
    
    @property
    def empate(self) -> bool:
        '''
        Getter de empate.

        Returns
        -------
        bool
            Retorna True si los jugadores empataron, y viceversa.

        '''
        return self.juego_empatado
    
    @property
    def ganador(self) -> str:
        '''
        Getter de ganador.

        Returns
        -------
        str
            String con el Jugador ganador de la partida.

        '''
        return self.jugador_ganador
    
    
    # Métodos
    
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
        
        '''Asigno cada número a los 4 palos inicializando las cartas'''
        for numero in self.valores:
            jerarquia+=1    # Aumento la jerarquía por cada iteración
            
            for palo in self.palos:
                carta = Carta(palo, numero, jerarquia)  # Creo una carta y le paso los parámetros correspondientes
                cartas.append(carta)    # Agrego la carta a la lista de cartas para crear luego el mazo
        
        '''Mezclo las cartas'''
        rd.seed(self._semilla)   # Asigno una semilla para que se mezcle de una forma en específico
        rd.shuffle(cartas)      # Mezclo las cartas
        
        '''Una vez mezcladas las cartas, las agrego al mazo'''
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
        
        for i in range(self.mazo.tamanio()//2):
            '''
            Iteración que se repite 26 veces, para repartir en cantidades
            iguales el mazo a cada jugador.
            '''

            '''Reparte carta al Jugador 1.'''
            self.mazo_jugador1.agregar_carta(self.mazo.sacar_carta())

            '''Reparte carta al Jugador 2.'''
            self.mazo_jugador2.agregar_carta(self.mazo.sacar_carta())
                
    
    def iniciar_juego(self):
        
        '''Se crea el mazo y se mezclan las cartas'''
        self.crear_mazo()
        
        '''Se reparten las cartas a cada jugador'''
        self.repartir()
        
        '''Inicializo los turnos jugados'''
        self.turnos = 0
        
        while self.turnos < self.cantidad_turnos:
            try:
                self.turnos += 1
                self.jugar(turno_actual = self.turnos, carta_jugador1 = self.mazo_jugador1.jugar_carta(), carta_jugador2 = self.mazo_jugador2.jugar_carta())
            
            except(ValueError):
                '''
                Si alguno de los 2 mazo ya no tiene cartas, 
                devuelve "ValueError, por ende, termina el juego
                '''
                pass
            
            if self.mazo_jugador1.tamanio() == 0:
                '''
                El Jugador 1 se queda sin cartas.
                Gana el Jugador 2 la partida.
                '''
                self.jugador_ganador = "jugador 2"
                print("\n\t\t\t\t|  Gana Jugador 2  |")
                break
            
            elif self.mazo_jugador2.tamanio() == 0:
                '''
                El Jugador 2 se queda sin cartas.
                Gana el Jugador 1 la partida.
                '''
                self.jugador_ganador = "jugador 1"
                print("\n\t\t\t\t|  Gana Jugador 1  |")
                break
            
            elif self.turnos == self.cantidad_turnos:
                '''
                Se llega a la cantidad límite de turnos.
                Se declara empate.
                '''
                self.juego_empatado = True
                print("\n\t\t\t\t\t|  Empate  |")
                break


    def jugar(self, turno_actual, carta_jugador1, carta_jugador2):
        
        '''Se colocan las cartas jugadas en la mesa'''
        self.cartas_mesa.append(carta_jugador1)
        self.cartas_mesa.append(carta_jugador2)
        

        if self.valores.index(carta_jugador1[0]) < self.valores.index(carta_jugador2[0]):
            '''Gana el turno el Jugador 2'''
            
            '''Muestro los mazos de ambos jugadores, y las cartas jugadas'''
            print('-------------------------------------------------------\n')
            
            print(f"Turno: {turno_actual}\n")
            
            print("Jugador 1:")
            # Muestro las cartas del mazo del jugador 1
            cartas = True
            cartas_restantes = self.mazo_jugador1.tamanio()
            while cartas:
                if cartas_restantes >= 10:
                    print("-X " * 10)
                    cartas_restantes -= 10
                else:
                    print("-X " * cartas_restantes)
                    cartas_restantes -= cartas_restantes
                    cartas = False
                    
            
            '''Muestro las cartas jugadas'''
            print(f"\n\t\t{carta_jugador1} {carta_jugador2}\n")
            
            print("Jugador 2: ")
            # Muestro las cartas del mazo del jugador 1
            cartas = True
            cartas_restantes = self.mazo_jugador2.tamanio()
            while cartas:
                if cartas_restantes >= 10:
                    print("-X " * 10)
                    cartas_restantes -= 10
                else:
                    print("-X " * cartas_restantes)
                    cartas_restantes -= cartas_restantes
                    cartas = False
            
            print('\n-------------------------------------------------------')
        
            '''Agrego las cartas que ganó el Jugador 2 a su mazo'''
            for carta in self.cartas_mesa:
                self.mazo_jugador2.ganar_carta(carta)
            
            '''Remuevo las cartas de la mesa'''
            self.cartas_mesa.clear()
        
        
        elif self.valores.index(carta_jugador1[0]) > self.valores.index(carta_jugador2[0]):
            '''Gana el turno el Jugador 1'''
            
            '''Muestro los mazos de ambos jugadores, y las cartas jugadas'''
            print('-------------------------------------------------------\n')
            
            print(f"Turno: {turno_actual}\n")
            print("Jugador 1:")
            # Muestro las cartas del mazo del jugador 1
            cartas = True
            cartas_restantes = self.mazo_jugador1.tamanio()
            while cartas:
                if cartas_restantes >= 10:
                    print("-X " * 10)
                    cartas_restantes -= 10
                else:
                    print("-X " * cartas_restantes)
                    cartas_restantes -= cartas_restantes
                    cartas = False
            
            '''Muestro las cartas jugadas'''
            print(f"\n\t\t{carta_jugador1} {carta_jugador2}\n")
            
            print("Jugador 2: ")
            # Muestro las cartas del mazo del jugador 1
            cartas = True
            cartas_restantes = self.mazo_jugador2.tamanio()
            while cartas:
                if cartas_restantes >= 10:
                    print("-X " * 10)
                    cartas_restantes -= 10
                else:
                    print("-X " * cartas_restantes)
                    cartas_restantes -= cartas_restantes
                    cartas = False
            
            print('\n-------------------------------------------------------')
        
            '''Agrego las cartas que ganó el Jugador 1 a su mazo'''
            for carta in self.cartas_mesa:
                self.mazo_jugador1.ganar_carta(carta)
            
            '''Remuevo las cartas de la mesa'''
            self.cartas_mesa.clear()
        
        
        elif self.valores.index(carta_jugador1[0]) == self.valores.index(carta_jugador2[0]):
            '''Entran en Guerra los jugadores'''
            
            carta_jugador1G = 0
            carta_jugador2G = 0
            
            '''Bucle donde se ejecuta la Guerra hasta que las cartas jugadas no sean iguales'''
            while carta_jugador1G == carta_jugador2G:
            
                if self.mazo_jugador1.tamanio()>=4 and self.mazo_jugador2.tamanio()>=4:
                    '''Ambos jugadores cuentan con cartas suficientes para la Guerra'''
                    
                    '''Muestro los mazos de ambos jugadores, y las cartas jugadas'''
                    print('-------------------------------------------------------')
                    print("\t\t\t\t\t\t|  GUERRA  |")
                    
                    print(f"Turno: {turno_actual}\n")
                    print("Jugador 1:")
                    # Muestro las cartas del mazo del jugador 1
                    cartas = True
                    cartas_restantes = self.mazo_jugador1.tamanio()-4   # Resto 4 cartas a las cartas restantes para mostrar en la mesa, ya que son parte del botín de la guerra
                    while cartas:
                        if cartas_restantes >= 10:
                            print("-X " * 10)
                            cartas_restantes -= 10
                        else:
                            print("-X " * cartas_restantes)
                            cartas_restantes -= cartas_restantes
                            cartas = False
                    
                    '''Botín de la guerra, cartas boca abajo en la mesa'''
                    for i in range(3):
                        self.cartas_mesa.append(self.mazo_jugador1.jugar_carta())
                        self.cartas_mesa.append(self.mazo_jugador2.jugar_carta())
                    
                    self.cartas_mesa.append(carta_jugador1G:=self.mazo_jugador1.jugar_carta())
                    self.cartas_mesa.append(carta_jugador2G:=self.mazo_jugador2.jugar_carta())
                    
                    print(f"\n\t\t{carta_jugador1} {carta_jugador2}", "-X " * 6, f"{carta_jugador1G} {carta_jugador2G}\n")
                    
                    print("Jugador 2: ")
                    # Muestro las cartas del mazo del jugador 1
                    cartas = True
                    cartas_restantes = self.mazo_jugador2.tamanio()-4   # Resto 4 cartas a las cartas restantes para mostrar en la mesa, ya que son parte del botín de la guerra
                    while cartas:
                        if cartas_restantes >= 10:
                            print("-X " * 10)
                            cartas_restantes -= 10
                        else:
                            print("-X " * cartas_restantes)
                            cartas_restantes -= cartas_restantes
                            cartas = False
                            
                    print('\n-------------------------------------------------------')
                    
                    '''Comparo las nuevas cartas jugadas'''
                    if self.valores.index(carta_jugador1G[0]) > self.valores.index(carta_jugador2G[0]):
                        '''
                        Gana la guerra el Jugador 1.
                        Agrego las cartas que ganó el Jugador 1 a su mazo.
                        '''
                        for carta in self.cartas_mesa:
                            self.mazo_jugador1.ganar_carta(carta)
                            
                        '''Remuevo las cartas de la mesa'''
                        self.cartas_mesa.clear()
        
                    elif self.valores.index(carta_jugador1G[0]) < self.valores.index(carta_jugador2G[0]):
                        '''
                        Gana la guerra el Jugador 2.
                        Agrego las cartas que ganó el Jugador 2 a su mazo.
                        '''
                        for carta in self.cartas_mesa:
                            self.mazo_jugador2.ganar_carta(carta)
                            
                        '''Remuevo las cartas de la mesa'''
                        self.cartas_mesa.clear()
                    
                    # Actualizo las cartas actuales jugadas
                    carta_jugador1 = carta_jugador1G
                    carta_jugador2 = carta_jugador2G
                
                
                elif self.mazo_jugador1.tamanio()<4 or self.mazo_jugador2.tamanio()<4:
                    '''Alguno de los 2 jugadores no cuenta con las cartas suficientes para la Guerra'''
                    
                    if self.mazo_jugador1.tamanio()<4:
                        '''Jugador 1 Pierde'''
                        perdedor = "Jugador 1"
                    else:
                        '''Jugador 2 Pierde'''
                        perdedor = "Jugador 2"
                    
                    '''Muestro los mazos de ambos jugadores, y las cartas jugadas'''
                    print('-------------------------------------------------------')
                    print("\t\t\t\t\t\t|  GUERRA  |")
                    
                    print(f"Turno: {turno_actual}\n")
                    print("Jugador 1:")
                    # Muestro las cartas del mazo del jugador 1
                    cartas = True
                    cartas_restantes = self.mazo_jugador1.tamanio()
                    while cartas:
                        if cartas_restantes >= 10:
                            print("-X " * 10)
                            cartas_restantes -= 10
                        else:
                            print("-X " * cartas_restantes)
                            cartas_restantes -= cartas_restantes
                            cartas = False
                            
                    '''Muestro las cartas jugadas'''
                    print(f"El {perdedor} no tiene las cartas suficientes para finalizar el turno\n")
                    print(f"\t\t{carta_jugador1} {carta_jugador2}\n")
                    
                    print("Jugador 2: ")
                    # Muestro las cartas del mazo del jugador 1
                    cartas = True
                    cartas_restantes = self.mazo_jugador2.tamanio()
                    while cartas:
                        if cartas_restantes >= 10:
                            print("-X " * 10)
                            cartas_restantes -= 10
                        else:
                            print("-X " * cartas_restantes)
                            cartas_restantes -= cartas_restantes
                            cartas = False
                    
                    print('\n-------------------------------------------------------')
                    
                    '''Agrego las cartas al Mazo del jugador ganador'''
                    
                    if perdedor == 'Jugador 1':
                        '''Gana Jugador 2. Agrego las cartas que ganó, a su mazo'''
                        for carta in self.cartas_mesa:
                            self.mazo_jugador2.ganar_carta(carta)
                        
                        '''Remuevo las cartas de la mesa'''
                        self.cartas_mesa.clear()
                        
                    elif perdedor == 'Jugador 2':
                        '''Gana Jugador 1. Agrego las cartas que ganó, a su mazo'''
                        for carta in self.cartas_mesa:
                            self.mazo_jugador1.ganar_carta(carta)
                        
                        '''Remuevo las cartas de la mesa'''
                        self.cartas_mesa.clear()
                    
                    #Cambio los valores de las variables temporales, para salir del while
                    carta_jugador1G = -1
                    carta_jugador2G = -2
                    

# Pruebas locales

if __name__ == "__main__":
    
    semilla = int(input("\nIngrese semilla para el Juego Guerra: "))
    
    juego1 = JuegoGuerra(semilla)
    
    juego1.iniciar_juego()
    