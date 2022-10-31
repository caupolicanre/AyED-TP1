from dividir_con_listas import dividir_datos

def Mezclador_listas(f1,f2):
    # with open(F,"w") as f:
    final=[]
    i1=0
    i2=0
    d1=f1[i1]
    d2=f2[i2]
    while d1 and d2:
        if d1<d2:
            aux=d1
            i1+=1
            if i1<len(f1)-1:
                d1=f1[i1]
                final.append(aux)
            else:
                break
        elif d2<d1:
            aux=d2
            i2+=1
            if i2<len(f2)-1:
                d2=f2[i2]
                final.append(aux)
            else:
                break
    return final
l1,l2=dividir_datos("datos.txt")
print(l1)
print(l2)
f=Mezclador_listas(l1,l2)
print(f)