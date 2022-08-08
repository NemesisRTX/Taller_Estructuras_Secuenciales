#Entradas
ce1=float(input("Ingrese calificación del parcial #1: "))
ce2=float(input("Ingrese calificación del parcial #2: "))
ce3=float(input("Ingrese calificación del parcial #3: "))
cef=float(input("Ingrese calificación del examen final: "))
ctf=float(input("Ingrese calificación del trabajo final: "))
#Caja Negra
pce=(((ce1+ce2+ce3)/3)*0.55)
pcef=(cef*0.30)
pctf=(ctf*0.15)
cf=(pce+pcef+pctf)
#Salidas
print(f"El porcentaje del promedio de los tres examenes parciales es de: {pce}, el promedio del examen final es: {pcef}, el promedio del trabajo final es de: {pctf}, calificación final: {cf}.")