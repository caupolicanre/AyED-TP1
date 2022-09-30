def dividir_datos(datos,archi1,archi2):
    with open(datos) as f,  open(archi1,"w") as f1, open(archi2,"w")as f2:
        d1=f.readline()
        f1.write(d1)
        d2=f.readline()
        nlista=1
        while d2:
            if d2<d1:
                if nlista==2:
                    nlista=1
                elif nlista==1:
                    nlista=2
            if nlista==2:
                f2.write(d2)              
            else:
                f1.write(d2)     
            d1 = d2
            d2 = f.readline()
       

dividir_datos("./datos.txt", "./f1.txt", "./f2.txt")
        
        