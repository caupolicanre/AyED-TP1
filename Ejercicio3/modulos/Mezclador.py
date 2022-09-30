def Mezclador_datos(f1,f2,F):
    with open(f1,"r") as f1, open(f2,"r") as f2, open(F,"w") as f:
        d1=f1.readline()
        d2=f2.readline()
        numSublistas=0
        Fin_proceso=True
        sublista1= True
        sublista2=True
        if d2 == '':
            while d1:
                daux = d1
                d1 = f1.readline() 
                f.write(daux) 
            return Fin_proceso
        else:
            while d1 and d2:
                while sublista1==True and sublista2==True:
                    if d1<d2:
                        daux=d1
                        d1=f1.readline()
                        f.write(daux)
                        if daux>d1:
                            sublista1=False
                    else:
                        daux=d2
                        d2=f2.readline()
                        f.write(daux)
                        if daux>d2:
                            sublista2=False
                if sublista1==False:
                    daux=d2
                    f.write(daux)
                    d2=f2.readline()
                    while daux<d2:
                        daux = d2
                        d2 = f2.readline()
                        f.write(daux)
                        sublista1=True
                elif sublista2==False:
                    daux=d1
                    f.write(daux)
                    d1=f1.readline()
                    while daux < d1:
                        daux = d1
                        d1 = f1.readline()
                        f.write(daux)
                        sublista2=True
            numSublistas+=1
            while d1=='' and  d2!='':  
                daux = d2
                d2 = f2.readline()
                f.write(daux)
                numSublistas+=1
            while d1!='' and d2=='':
                daux = d1
                d1 = f1.readline()
                f.write(daux)
                numSublistas+=1
            
if __name__=='__main__':
    Mezclador_datos("f1.txt","f2.txt", "mezclados.txt")
    
            
            
            
            