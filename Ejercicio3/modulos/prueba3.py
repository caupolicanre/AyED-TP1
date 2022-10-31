from dividir import leer_Archivo
from dividir import dividir_datos
def Mezclador_listas(f1,f2):
    # with open(F,"w") as f:
    final=[]
    i1=0
    i2=0
    k=0
    # d1=f1[i1]
    # d2=f2[i2]
    while i1 < len(f1) and i2 < len(f2):
       if f1[i1] <= f2[i2]:
          final.append(f1[i1])
          i1 += 1
       else:
          final.append(f2[i2])
          i2 += 1
       k += 1
      
    while i1 < len(f1):
        final.append(f1[i1])
        i1 += 1
        k += 1
      
    while i2 < len(f2):
        final.append(f2[i2])
        i2 += 1
        k += 1
    return final



f=leer_Archivo("datos.txt")
print(f)
f1,f2=dividir_datos(f)
print(f1,f2)
f=Mezclador_listas(f1, f2)
print(f)

