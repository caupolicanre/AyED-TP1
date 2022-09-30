from Dividir_Datos import dividir_datos
from Mezclador import Mezclador_datos

with open("datos.txt","r+"), open("f1.txt","r+"),open("f2.txt","r+"),open("mezclados.txt","r+"):
    data=0
    while data != "ordenda":    
    
        datos = dividir_datos("datos.txt","f1.txt","f2.txt")
    
        data = Mezclador_datos("f1.txt","f2.txt","mezclados.txt")
        if data == True:
            break    
