# Importo la LDE para inicializar la Cola Doble
from Ejercicio1.modulos.LDE import ListaDobleEnlazada

class ColaDoble():
    def  __init__(self):
        self.items = ListaDobleEnlazada()
        
    def tamanio(self):
        '''
        Método para conocer el tamaño de la Cola Doble.

        Returns
        -------
        int
            Retorna tamaño de la Cola Doble.

        '''
        return self.items._tamanio
    
    def __str__(self):
        '''
        Muestra todos los Nodos de la Cola Doble.

        Returns
        -------
        string
            Retorna una lista de los Nodos dentro 
            de la Cola Doble.

        '''
        lista = [str(nodo) for nodo in self]
        return str(lista)
    
    def __iter__(self):
        '''
        Método para iterar la Cola Doble.
        '''
        return iter(self.items)
    
    def esta_vacia(self):
        '''
        Comprueba si el tamaño de la Cola Doble
        es igual a 0.
        
        Returns
        -------
        boolean
            Devuelve True si la Cola Doble está vacía.
        
        '''
        return self.items.esta_vacia()
    
    
    def agregar_frente(self, item):
        '''
        Agrega un nuevo ítem al frente de la Cola Doble.
        
        Parameters
        ----------
        item : any type
            Dato que se va a almacenar en un nuevo Nodo.
       
        Returns
        -------
        None.
        
        ''' 
        return self.items.anexar(item)
    
    
    def agregar_final(self, item):
        '''
        Agrega un nuevo ítem al final de la Cola Doble.
       
        Parameters
        ----------
        items : any type
            Dato que se va a almacenar en un nuevo Nodo.
        
        Returns
        -------
        None.
        
        ''' 
        return self.items.agregar(item)
    
    
    def remover_frente(self):
        ''' 
        Elimina el ítem del frente de la Cola Doble 
        y lo devuelve.
        
        Returns
        -------
        temp : reference
            Retorna el ítem extraido de la Cola Doble.
             
        '''
        return self.items.extraer(self.items.tamanio-1)
    
    
    def remover_final(self):
       ''' 
       Elimina el ítem del final de la Cola Doble 
       y lo devuelve.
       
       Returns
       -------
       temp : reference
           Retorna el ítem extraido de la Cola Doble.
            
       '''
       return self.items.extraer(0)    
        
    


if __name__=='__main__':
    
    pruebaColaDoble= ColaDoble()
    
    pruebaColaDoble.agregar_final(25)
    pruebaColaDoble.agregar_final(6)
    pruebaColaDoble.agregar_frente(8)
    
    print(pruebaColaDoble)
    print(pruebaColaDoble.remover_final())
    
    print(pruebaColaDoble)
    print(pruebaColaDoble.remover_frente())
    
    print(pruebaColaDoble)
    
