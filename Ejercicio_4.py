#Entradas
compra=float(input("Ingrese el valor de la compra: "))
#Caja Negra
descuento=(compra*0.15)
total=(compra-descuento)
#Salidas
print(f"El valor a pagar con el descuento aplicado es de: ${total}")