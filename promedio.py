n = int(input("Ingrese la cantidad de alturas: "))
alturas = []

for i in range(n):
    altura = float(input(f"Ingrese la altura de la persona {i+1}: "))
    alturas.append(altura)

promedio_alturas = sum(alturas) / n

print("La altura promedio de las personas es:", promedio_alturas)