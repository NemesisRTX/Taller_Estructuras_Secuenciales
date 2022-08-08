#Entradas
h=int(input("Ingrese cantidad de hombres: "))
m=int(input("Ingrese cantidad de mujeres: "))
#Caja Negra
total=(h+m)
ph=((h/total)*100)
pm=((m/total)*100)
#Salidas
print(f"El porcentaje de hombres en el grupo es de {ph} mientras que el porcentaje de mujeres es de {pm} en el grupo de {total} estudiantes.")