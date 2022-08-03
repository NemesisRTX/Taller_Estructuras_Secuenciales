#Entradas
m1=float(input("Ingrese nota de tarea #1 de matemáticas: "))
m2=float(input("Ingrese nota de tarea #2 de matemáticas: "))
m3=float(input("Ingrese nota de tarea #3 de matemáticas: "))
me=float(input("Ingrese nota del examen de matemáticas: "))
f1=float(input("Ingrese nota de tarea #1 de física: "))
f2=float(input("Ingrese nota de tarea #2 de física: "))
fe=float(input("Ingrese nota del examen de física: "))
q1=float(input("Ingrese nota de tarea #1 de química: "))
q2=float(input("Ingrese nota de tarea #2 de química: "))
q3=float(input("Ingrese nota de tarea #3 de química: "))
qe=float(input("Ingrese nota del examen de química: "))
#Caja Negra
pmt=((m1+m2+m3)/3)*0.10
pme=me*0.90
pft=((f1+f2)/2)*0.20
pfe=fe*0.80
pqt=((q1+q2+q3)/3)*0.15
pqe=qe*0.85
pm=(pmt+pme)
pf=(pft+pfe)
pq=(pqt+pqe)
pg=(pm+pf+pq)/3
#Salidas
print(f"El promedio de matemáticas es de: {pm} ")
print(f"El promedio de física es de: {pf}")
print(f"El promedio de química es de: {pq}")
print(f"El promedio general es de: {pg}")
