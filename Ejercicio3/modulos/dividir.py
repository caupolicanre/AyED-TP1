def leer_Archivo(archivo):
    with open(archivo) as archi:
        archivo = archi.read().splitlines()
        for i in range(len(archivo)):
            archivo[i]=int(archivo[i])
            
    return archivo

def dividir_datos(f):
    d1=f[0]
    d2=f[1]
    i=1
    f1=[d1]
    f2=[]
    nlista=1
    while d2:
        if d2<d1:
            if nlista==2:
                nlista=1
            elif nlista==1:
                nlista=2
        if nlista==2:
            f2.append(d2)              
        else:
            f1.append(d2)    
        i+=1
        if i>=len(f):
            break
        d1 = d2
        d2 = f[i]
    return f1,f2
def Mezclador_listas(f1,f2):
    # with open(F,"w") as f:
    final=[]
    i1=0
    i2=0
    i3=0
    # d1=f1[i1]
    # d2=f2[i2]
    while i1 < len(f1) and i2 < len(f2):
       if f1[i1] <= f2[i2]:
          final.append(f1[i1])
          i1 += 1
       else:
          final.append(f2[i2])
          i2 += 1
       i3 += 1
      
    while i1 < len(f1):
        final.append(f1[i1])
        i1 += 1
        i3 += 1
      
    while i2 < len(f2):
        final.append(f2[i2])
        i2 += 1
        i3 += 1
    return final



f=leer_Archivo("datos.txt")
f1,f2=dividir_datos(f)
while f2!=[]:
    f=Mezclador_listas(f1, f2)
    f1,f2=dividir_datos(f)
print(f)

