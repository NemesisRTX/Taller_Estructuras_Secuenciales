#Entradas
sueldo=float(input("Ingrese sueldo base: "))
#Caja Negra
extra=(sueldo*0.10)
ventas=(extra*3)
total=(sueldo+ventas)
#Salidas
print(f"La comision que se obtiene por concepto de tres ventas es de ${ventas} para un total de: ${total}")