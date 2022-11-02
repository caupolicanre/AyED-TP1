from dividir import dividir_datos
from Mezclador import mezclar_datos
with open("datos.txt") as datos, open("f1.txt","w") as f1, open("f2.txt","w")as f2:

    data = 0
    while data != "ordenda":
    
        datos = dividir_datos("./datos.txt","./f1.txt","./f2.txt")

        archis = mezclar_datos("./f1.txt", "./f2.txt", "./datos.txt")
        if archis == True:
            break
with open("f1.txt","r")as f1:
    with open("Mezclados.txt","w")as mezcla:
        for linea in f1:
            mezcla.write(linea)