def dividir_datos(datos):
    f1=[]
    f2=[]
    with open(datos) as f:
        d1=f.readline()
        f1.append((int(d1.strip("\n"))))
        d2=f.readline()
        nlista=1
        while d2:
            if d2<d1:
                if nlista==2:
                    nlista=1
                elif nlista==1:
                    nlista=2
            if nlista==2:
                f2.append((int(d2.strip("\n"))))              
            else:
                f1.append((int(d2.strip("\n"))))    
            d1 = d2
            d2 = f.readline()
    return f1,f2

dividir_datos("datos.txt")
        
        