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
            while d1 and d2:    #mientras existan datos en d1 y d2 
                
                if d2 < d1:
                    aux = d2
                    d2 = f2.readline()
                    if d2 < aux:
                        
                        sublistaf2 = False 
                else:
                    aux = d1
                    d1 = f1.readline()       
                    if d1 < aux:
                        
                        sublistaf1 = False
                        
                if sublistaf1 == False:
                    f.write(aux)
                    while aux < d2:
                        aux = d2
                        d2 = f2.readline()
                        f.write(aux)
                    
                    
                elif sublistaf2 == False:
                    f.write(aux)
                    while aux < d1:
                        aux = d1
                        d1 = f1.readline()
                        f.write(aux)
                    
                if sublistaf1 != False and sublistaf2 != False:
                    f.write(aux)
                else:
                    sublistaf1 = True    
                    sublistaf2 = True
                
            while d1 == '' and d2 != '':  
                aux = d2
                d2 = f2.readline()
                f.write(aux)
                
            while d2 == '' and d1 != '':
                aux = d1
                d1 = f1.readline()
                f.write(aux)