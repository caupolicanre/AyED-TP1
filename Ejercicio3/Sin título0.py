with open("a.txt","r") as archi:
    archivo = archi.read().splitlines()
a=len(archivo)
c=a//2
print(c)