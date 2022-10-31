def Mezclador_datos(f1,f2,F):
    with open(f1,"r") as f1, open(f2,"r") as f2, open(F,"w") as f:
        d1=f1.readline()
        d2=f2.readline()
        # daux1=0
        # daux2=0
        aux=0
        while d1 and d2:
            if d1<d2:
                aux=d1
                d1=f1.readline()
                f.write(aux)                                   
            elif d2<d1:
                aux=d2
                d2=f2.readline()
                f.write(aux)
            if f2.readline()<d2:
                while f1.readline()>d1:
                    aux=d1
                    d1=f1.readline()
                    f.write(d1)
            elif f1.readline()<d1:
                while f2.readline()>d2:
                    aux=d2
                    d2=f2.readline()
                    f.write(d2)

if __name__=='__main__':
    Mezclador_datos("f1.txt","f2.txt", "mezclados.txt")
               