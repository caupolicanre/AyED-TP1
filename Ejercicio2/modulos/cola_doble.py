from LDE import ListaDobleEnlazada

class ColaDoble():
    def  __init__(self):
        self.item= ListaDobleEnlazada()
        
        
        
    # Propiedades
    
    @property
    def tamanio(self):
        '''
        

        Returns
        -------
        int
            Retorna tamaño de la Cola Doble.

        '''
        return self.item._tamanio
    
    def __str__(self):
        '''
        

        Returns
        -------
        string
            Retorna una lista de los Nodos dentro 
            de la Cola Doble.

        '''
        return self.item.__str__()
    
    def esta_vacia(self):
        '''
        Comprueba si el tamaño de la Lista es igual a 0.
        
        Returns
        -------
        boolean
            Devuelve True si la Lista está vacía.
        
        '''
        return self.item.esta_vacia()
    
    
    def agregarFrente(self,item):
        '''
        Agrega un nuevo ítem al final de la Cola Doble.
        
        Parameters
        ----------
        item : any type
            Dato que se va a almacenar en un nuevo Nodo.
       
        Returns
        -------
        None.
        
        ''' 
        return self.item.anexar(item)
    
    
    def agregarFinal(self,item):
        '''
        Agrega un nuevo ítem al inicio de la Cola Doble.
       
        Parameters
        ----------
        item : any type
            Dato que se va a almacenar en un nuevo Nodo.
        
        Returns
        -------
       
        None.
        
        ''' 
        return self.item.agregar(item)
    
    
    def removerFrente(self):
        
        ''' 
         Elimina y devuelve el ítem de la última posición.
        
         Returns
         -------
         temp : reference
             Retorna el ítem extraido de la Cola Doble.
        '''
        return self.item.extraer(self.item.tamanio-1)
    
    
    def removerFinal(self):
       ''' 
        Elimina y devuelve el ítem de la primera posición.
       
        Returns
        -------
        temp : reference
            Retorna el ítem extraido de la Cola Doble.
            
       '''
       return self.item.extraer(0)    
        
    






if __name__=='__main__':
    pruebaColaDoble= ColaDoble()
    pruebaColaDoble.agregarFinal(25)
    pruebaColaDoble.agregarFinal(6)
    pruebaColaDoble.agregarFrente(8)
    print(pruebaColaDoble)
    print(pruebaColaDoble.removerFinal())
    print(pruebaColaDoble)
    print(pruebaColaDoble.removerFrente())
    print(pruebaColaDoble)
    
