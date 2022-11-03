def mezclar_datos(f1,f2,F):
    with open(f1,"r") as f1, open(f2,"r") as f2, open(F, "w")as f:
        d1 = f1.readline()        # es el primer dato de f1
        d2 = f2.readline()        # es el primer dato de f2
        aux = d1             # es el dato que queremos escribir en la lista de salida 
        ordenada = True
        sublistaf1 = True
        sublistaf2 = True
        if d2 == '':
            while d1:
                aux = d1
                d1 = f1.readline() 
                f.write(aux) 
            return ordenada
        else:    
            while d1 and d2:    
                '''
                 Mientras existan datos en d1 y d2
                '''
                if d2 < d1:
                    '''
                    Si el dato(d2) en el archivo 2 es menor al dato(d1) en el archivo 1
                    que se va a guardar el valor de d2 en una variable aux y se toma el siguiente valor
                    si este valor es menor al anterior termina la sublista.
                    '''
                    aux = d2
                    d2 = f2.readline()
                    if d2 < aux:
                        
                        sublistaf2 = False 
                else:
                    '''
                    Se  guarda el valor de d1 en aux y se toma el siguiente valor
                    si este valor es menor al anterior termina la sublista.
                    '''
                    aux = d1
                    d1 = f1.readline()       
                    if d1 < aux:
                        
                        sublistaf1 = False
                        
                if sublistaf1 == False:
                    '''
                    Si se termino la sub lista escribir el resto de la sublista
                    de f2 hasta que esta tambien se termine.
                    '''
                    f.write(aux)
                    while aux < d2:
                        aux = d2
                        d2 = f2.readline()
                        f.write(aux)
                    
                    
                elif sublistaf2 == False:
                    '''
                    Si se termino la sublista en f1 escribir el resto de la sublista
                    de el archivo2 hasta que esta tambien se termine
                    '''
                    f.write(aux)
                    while aux < d1:
                        aux = d1
                        d1 = f1.readline()
                        f.write(aux)
                    
                if sublistaf1 != False and sublistaf2 != False:
                    '''
                    Actualizacion de las sublistas
                    '''
                    f.write(aux)
                else:
                    sublistaf1 = True    
                    sublistaf2 = True
                
            while d1 == '' and d2 != '':  
                '''
                Si f2 se queda sin datos pero aun hay datos en f1
                se agregan los datos restantes hasta que 
                no haya mas datos en ninguno de los dos archivos.
                '''
                aux = d2
                d2 = f2.readline()
                f.write(aux)
                
            while d2 == '' and d1 != '':
                '''
                Si f1 se queda sin datos pero aun hay datos en f1
                se agregan los datos restantes hasta que 
                no haya mas datos en ninguno de los dos archivos.
                '''
                aux = d1
                d1 = f1.readline()
                f.write(aux)