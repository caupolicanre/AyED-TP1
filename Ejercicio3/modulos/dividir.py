def dividir_datos(archivo,F1,F2):
    with open(archivo) as datos, open(F1,"w") as f1, open(F2,"w")as f2:
        d1 = datos.readline()
        f1.write(d1)
        d2 = datos.readline()
        aux = f1
        
        while d2:   #mientras exista
            if d2<d1:
                if aux == f2:
                    aux = f1
                else:
                    aux = f2
                    
            aux.write(d2)
            d1 = d2
            d2 = datos.readline()