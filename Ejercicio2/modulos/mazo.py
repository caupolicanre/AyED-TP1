# Importo Cola Doble para la implementaciÃ³n del Mazo
from cola_doble import ColaDoble

# Importaciones para pruebas locales
import random as rd


class Carta:
    
    def __init__(self, palo, numero, jerarquia, cara = "Boca abajo"):
        self._palo = palo
        self._numero = numero
        self._jerarquia = jerarquia 
        self._cara = cara
        
        
    # Métodos mágicos
    
    def __str__(self):
        if self._cara == "Boca abajo":
            return "-X"
        else:
            return str(self._numero) + str(self._palo)
    
    def __lt__(self, other):
        return self._jerarquia < other._jerarquia
    
    def __gt__(self, other):
        return self._jerarquia > other._jerarquia

    def __eq__(self, other):
        return self._jerarquia == other._jerarquia
    
    def __getitem__(self, indice):
        return self._numero[indice]
            

    # Propiedades
    
    @property
    def palo(self):
        return self._palo
    
    @property
    def numero(self):
        return self._numero
        
    @property
    def jerarquia(self):
        return self._jerarquia
    
    @property
    def cara(self):
        return self._cara
    
    @cara.setter
    def cara(self, nueva_cara):
        self._cara = nueva_cara


class Mazo:
    
    def __init__(self):
        self.mazo = ColaDoble()
    
    # Métodos Mágicos
    
    def __str__(self):
        return str(self.mazo)
    
    def __iter__(self):
        return iter(self.mazo)
    
    
    # Métodos
    
    def tamanio(self):
        '''
        Método para conocer el tamaño del Mazo.

        Returns
        -------
        int
            Retorna tamaño del Mazo.

        '''
        return self.mazo.tamanio()
    
    def agregar_carta(self, carta_nueva):
        '''
        Recibe una carta, y la agrega al mazo.

        Parameters
        ----------
        carta_nueva : class
            Recibe una carta.

        Returns
        -------
        None.

        '''
        self.mazo.agregar_frente(carta_nueva)
        
    def jugar_carta(self, estado_cara = "Boca abajo"):
        '''
        Remueve la carta que se encuentra en el frente del mazo,
        y la devuelve. Dependiendo del estado, estará Boca arriba,
        o Boca abajo.

        Parameters
        ----------
        estado_cara : class, opcional
            Si los jugadores están en guerra, se juega la carta
            "Boca abajo", sino, se recibe como parámetro "Boca arriba".
            Por defecto la cara de la carta es "Boca abajo".

        Returns
        -------
        carta_jugada : class
            Retorna la carta que se jugó.

        '''
        carta_jugada = self.mazo.remover_frente()
        carta_jugada._cara = estado_cara
        
        return carta_jugada
    
    def ganar_carta(self, carta_ganada):
        '''
        Agrega al final del Mazo del jugador la carta que ganó.

        Parameters
        ----------
        carta_ganada : class
            Carta que ganada que se agregará al Mazo del jugador.

        Returns
        -------
        None.

        '''
        self.mazo.agregar_final(carta_ganada._dato)

    def sacar_carta(self):
        '''
        Remueve una carta del mazo.

        Returns
        -------
        class
            Retorna la carta que se removió.

        '''
        return self.mazo.remover_frente()



# Pruebas locales

if __name__ == "__main__":
    
    carta1 = Carta(palo="♥", numero=5, cara="Boca abajo")
    print(carta1)
    
    carta2 = Carta(palo="♠", numero=10, cara="Boca arriba")
    print(carta2)
    
    mazo = Mazo()
    mazoJ1 = Mazo()
    mazoJ2 = Mazo()
    
    '''Crear Mazo'''
    
    valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    palos = ['â ', 'â¥', 'â¦', 'â£']
    cartas = []     # Lista para guardar las cartas, mezclarlas y luego crear un mazo
    jerarquia = 0   # Utilizo una jerarquÃÂ­a para comparar luego las cartas
        
    # Asigno cada nÃÂºmero a los 4 palos
    for numero in valores:
        jerarquia+=1    # Aumento la jerarquÃÂ­a por cada iteraciÃÂ³n
        
        for palo in palos:
            carta = Carta(palo, numero, jerarquia, "Boca arriba")  # Creo una carta y le paso los parÃÂ¡metros correspondientes
            cartas.append(carta)    # Agrego la carta a la lista de cartas para crear luego el mazo
        
    rd.shuffle(cartas)      # Mezclo las cartas
        
    # Una vez mezcladas las cartas, las agrego al mazo
    for carta in cartas:
        mazo.agregar_carta(carta)
        
    print("\nMazo:\n", mazo)
    
    
    
    '''Repartir cartas'''
    
    for i, carta in enumerate(mazo):
        '''
        Si "i" es par, la carta va al mazo del Jugador 1,
        si es impar, la carta va al mazo del Jugador 2.
        '''
        if i%2 == 0:
            mazoJ1.agregar_carta(carta)
                
        if i%2 != 0:
            mazoJ2.agregar_carta(carta)
                
    
    print("\nMazo Jugador 1:\n", mazoJ1)
    print("\nMazo Jugador 2:\n", mazoJ2)
