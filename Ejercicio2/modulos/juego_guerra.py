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
        
        self.turnos_jugados = 1
        self.cantidad_turnos = 10000    # Límite de turnos
        
        self.ganador = None
        self.empate = True
        
    
    
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

        cartas = []     # Lista para guardar las cartas, mezclarlas y luego crear
        jerarquia = 0
        
        '''Asigno cada número a los 4 palos inicializando las cartas'''
        for numero in self.valores:
            jerarquia += 1
            for palo in self.palos:
                carta = Carta(palo, numero, jerarquia, "Boca arriba")    # Inicializo una clase Carta con los datos generados
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
        '''
        Función donde se procesa cada parte del Juego Guerra.
        Requerida para el test, ya que es la única función a la
        que llama.

        Returns
        -------
        None.

        '''
        
        '''Se crea el mazo y se mezclan las cartas'''
        self.crear_mazo()
        
        '''Se reparten las cartas a cada jugador'''
        self.repartir()
        
        '''Comienza la simulación del juego'''
        self.jugar()
        
                    

    def mostrar_mazo(self, cartas_restantes: int):
        '''
        Muestra por consola las cartas restantes del mazo de un jugador.
        Con el formato de 10 cartas como máximo por ilera.

        Parameters
        ----------
        cartas_restantes : int
            Cartas restantes en el mazo del jugador.

        Returns
        -------
        None.

        '''
        cartas = True
        cartas_restantes = cartas_restantes
        
        while cartas:
            if cartas_restantes >= 10:
                print("-X " * 10)
                cartas_restantes -= 10
            else:
                print("-X " * cartas_restantes)
                cartas_restantes -= cartas_restantes
                cartas = False


    def jugar(self):
        '''
        Compara las cartas en cada turno, llama al método
        "mostrar_mazo" para mostrar por pantalla los mazos de los
        jugadores.

        Returns
        -------
        None.

        '''
        while self.turnos_jugados <= self.cantidad_turnos:
            
            try:
                carta_jugador1 = self.mazo_jugador1.jugar_carta("Boca arriba")
                carta_jugador2 = self.mazo_jugador2.jugar_carta("Boca arriba")
                
                self.cartas_mesa.append(carta_jugador1)
                self.cartas_mesa.append(carta_jugador2)
                
                print('-------------------------------------------------------')
                print(f"\nTurno: {self.turnos_jugados}\n")  
                print("Jugador 1:")
                self.mostrar_mazo(self.mazo_jugador1.tamanio())     # Muestro las cartas del mazo del jugador 1
                
                # Muestro las cartas jugadas
                print(f"\n\t\t{carta_jugador1} {carta_jugador2}\n")
                
                print("Jugador 2: ")
                self.mostrar_mazo(self.mazo_jugador2.tamanio())     # Muestro las cartas del mazo del jugador 2
                
                
                if carta_jugador1 > carta_jugador2:
                    '''Gana ronda Jugador 1'''
                    for carta in self.cartas_mesa:
                        self.mazo_jugador1.ganar_carta(carta)
                
                
                elif carta_jugador1 < carta_jugador2:
                    '''Gana ronda Jugador 2'''
                    for carta in self.cartas_mesa:
                        self.mazo_jugador2.ganar_carta(carta)
                
                
                elif carta_jugador1 == carta_jugador2:
                    '''Las cartas son iguales. Entran en Guerra'''
                    
                    while carta_jugador1 == carta_jugador2:
                        '''Mientras los jugadores sigan en Guerra, se ejecuta esta parte de la simulación'''
                        
                        # Variables auxiliares para mostrar en la mesa
                        carta_jugador1_guerra = carta_jugador1
                        carta_jugador2_guerra = carta_jugador2
                        
                        for _ in range(3):
                            self.cartas_mesa.append(self.mazo_jugador1.jugar_carta())
                            self.cartas_mesa.append(self.mazo_jugador2.jugar_carta())
                        
                        carta_jugador1 = self.mazo_jugador1.jugar_carta("Boca arriba")
                        carta_jugador2 = self.mazo_jugador2.jugar_carta("Boca arriba")
                        self.cartas_mesa.append(carta_jugador1)
                        self.cartas_mesa.append(carta_jugador2)
                        
                        print('-------------------------------------------------------')
                        print("\t\t\t\t\t\t|  GUERRA  |")
                        print(f"Turno: {self.turnos_jugados}\n")  
                        print("Jugador 1:")
                        self.mostrar_mazo(self.mazo_jugador1.tamanio())
                        
                        # Muestro las cartas jugadas
                        print(f"\n\t\t{carta_jugador1_guerra} {carta_jugador2_guerra}", "-X " * 6, f"{carta_jugador1} {carta_jugador2}\n")
                        
                        print("Jugador 2: ")
                        self.mostrar_mazo(self.mazo_jugador2.tamanio())


                    if carta_jugador1 > carta_jugador2:
                        '''Gana ronda Jugador 1'''
                        for carta in self.cartas_mesa:
                            self.mazo_jugador1.ganar_carta(carta)
                    
                    elif carta_jugador1 < carta_jugador2:
                        '''Gana ronda Jugador 2'''
                        for carta in self.cartas_mesa:
                            self.mazo_jugador2.ganar_carta(carta)
            
            
            except:
                
                if self.mazo_jugador1.tamanio() == 0:
                    '''
                    El Jugador 1 se queda sin cartas.
                    Gana el Jugador 2 la partida.
                    '''
                    self.ganador = "jugador 2"
                    print('-------------------------------------------------------')
                    print("\n\t\t\t\t|  Gana Jugador 2  |")
                
                if self.mazo_jugador2.tamanio() == 0:
                    '''
                    El Jugador 2 se queda sin cartas.
                    Gana el Jugador 1 la partida.
                    '''
                    self.ganador = "jugador 1"
                    print('-------------------------------------------------------')
                    print("\n\t\t\t\t|  Gana Jugador 1  |")
                
                break
            
            
            finally:
                '''
                Esta parte se ejecuta siempre.
                Sumo 1 al contador de turnos, y remuevo las cartas de la mesa.
                '''
                
                self.turnos_jugados += 1
                self.cartas_mesa.clear()
        
        if self.turnos_jugados >= self.cantidad_turnos:
            self.empate = True
            print('-------------------------------------------------------')
            print("\n\t\t\t\t\t\t|  Empate  |")

# Pruebas locales

if __name__ == "__main__":
    
    semilla = int(input("\nIngrese semilla para el Juego Guerra: "))
    
    juego1 = JuegoGuerra(semilla)
    
    juego1.iniciar_juego()
    