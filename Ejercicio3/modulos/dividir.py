import prueba3
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

# f=leer_Archivo("datos.txt")
# print(f)
# f1,f2=dividir_datos(f)
# print(f1,f2)
# f=prueba3.Mezclador_listas(f1, f2)
# print(f)
        