import math
#Entradas
a=float(input("Insertar lado A: "))#float
b=float(input("Insertar lado B: "))#float
c=float(input("Insertar lado C: "))#float
#Caja Negra
s=(a+b+c)/2#float
area=math.sqrt(s*(s-a)*(s-b)*(s-c))#float
#Salidas
print("El área es: "+str(area))