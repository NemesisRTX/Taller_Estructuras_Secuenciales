#Entradas
horas=int(input("Ingrese horas de trabajo: "))
precioh=float(input("Ingrese precio de la hora: "))
#Caja Negra
sbase=(horas*precioh)
sneto=(sbase*0.80)
#Salidas
print(f"El salario neto es de: ${sneto}")