#Entradas
nombre=str(input("Ingrese nombre del trabajador: "))
hijos=int(input("Ingrese numero de hijos del trabajador: "))
hogares=int(input("Ingrese numero de hogares del trabajador: "))
act=int(input("Ingrese la cantidad de actualizaciones academicas del trabajador: "))
nhoras=int(input("Ingrese numero de horas de trabajo: "))
phoras=float(input("Ingrese el precio por una hora: "))
ehoras=int(input("Ingrese numero de horas extra: "))
#Caja Negra
pehoras=(ehoras*0.25)
sbase=(nhoras*phoras)
d1=(sbase*0.95)
d2=(sbase*0.98)
d3=(sbase*0.93)
dt=(d1+d2+d3)
a1=(sbase+250000*act)
a2=(sbase+173000*hijos)
a3=(sbase+180000*hogares)
at=(a1+a2+a3)
sneto=(sbase+pehoras+dt+at)
#Salidas
print(f"Las deducciones sobre el sueldo son de ${dt}.")
print(f"Las asignaciones sobre el sueldo son de ${at}.")
print(f"El sueldo neto de {nombre} es: ${sneto}.")