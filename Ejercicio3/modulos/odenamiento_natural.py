class Mezcla_Natural:
  def __init__(self, archivo):
    self.archivo = archivo
    self.tamanio = len(archivo)
    self.guardar = archivo
    
    
  def abrir_archivo(self):
      """
      Abre el archivo que recibe como parámetro, lee su contenido y lo 
      guarda como una lista.
      
      """
      with open(self.archivo , 'r') as archi: 
           self.archivo = archi.read().splitlines()
           

  def ordenar(self):
      """
      Algoritmo de ordenamiento Mezcla Natural

     
      """      
      if self.tamanio <= 1:
          return
        
      mitad = self.tamanio // 2
        
      izq = Mezcla_Natural(self.archivo[:mitad])
      der = Mezcla_Natural(self.archivo[mitad:])
                
      izq.ordenar()
      der.ordenar()
      
      j= 0 
      i = 0
      k = 0
        
      while i < len(izq.archivo ) and j < len(der.archivo):
         if izq.archivo[i] <= der.archivo[j]:
            self.archivo[k] = izq.archivo[i]
            i += 1
         else:
            self.archivo[k] = der.archivo[j]
            j += 1
         k += 1
        
      while i < len(izq.archivo):
          self.archivo[k] = izq.archivo[i]
          i += 1
          k += 1
        
      while j < len(der.archivo):
          self.archivo[k] = der.archivo[j]
          j += 1
          k += 1
       
   
  def guardar_archivo(self):
      """
      Guarda el archivo luego de ser ordenado
      
      """
      with open(self.guardar, 'w') as archi: 
           for linea in self.archivo: 
               archi.write(linea + '\n')



if __name__ == '__main__': 
    
    a=Mezcla_Natural("datos.txt")
    a.abrir_archivo()
    a.ordenar()
    a.guardar_archivo()
