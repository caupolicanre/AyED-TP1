from cola_doble import ColaDoble

# Importaciones para pruebas locales
from carta import Carta
import random as rd


class Mazo:
    
    def __init__(self):
        self.mazo = ColaDoble()
    
    def __str__(self):
        return self.mazo.__str__()
    
    def __iter__(self):
        return iter(self.mazo)
    
    def agregar_carta(self, cartaNueva):
        '''
        Recibe una carta, y la agrega al mazo.

        Parameters
        ----------
        cartaNueva : class
            Recibe una carta.

        Returns
        -------
        None.

        '''
        self.mazo.agregarFinal(cartaNueva)

    def jugar_carta(self, estadoCara="Boca abajo"):
        '''
        Remueve la carta que se encuentra en el tope del mazo,
        y la devuelve. Dependiendo del estado, estará Boca arriba,
        o Boca abajo.

        Parameters
        ----------
        estadoCara : class, opcional
            Si los jugadores están en guerra, se deja la carta
            boca abajo, sino se recibe como parámetro "Boca arriba".
            Por defecto la cara de la carta es "Boca abajo".

        Returns
        -------
        cartaJugada : class
            Retorna la carta que se jugó.

        '''
        cartaJugada = self.mazo.removerFinal()
        cartaJugada.estadoCara = estadoCara
        
        return cartaJugada
    
    def jugador_gana(self, cartasGanadas):
        self.mazo



# Pruebas locales

if __name__ == "__main__":
    
    mazo = Mazo()
    mazoJ1 = Mazo()
    mazoJ2 = Mazo()
    
    '''Crear Mazo'''
    
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