#Entradas
nume1=float(input("Ingrese cantidad de chelines austriacos para convertir a pesetas: "))
nume2=float(input("Ingrese cantidad de dracmas griegos para convertir a francos franceses: "))
nume3=float(input("Ingrese cantidad de pesetas para convertir a dólares y liras italianas: "))
#Caja Negra
pesetas=((nume1*956.871)/100)
francos=((nume2*88.607)/(100*20.110))
dolares=(nume3/122.499)
liras=((nume3*100)/9.289)
#Salidas
print(f"${nume1} chelines austriacos equivalen a: ${pesetas} pesetas.")
print(f"${nume2} dracmas griegos equivalen a: ${francos} francos.")
print(f"${nume3} pesetas equivalen a: ${dolares} dolares.")
print(f"${nume3} pesetas equivalen a: ${liras} liras.")