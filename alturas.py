n = int(input("Ingrese el número de personas: "))

suma_alturas = 0

for i in range(n):
    altura = float(input(f"Ingrese la altura de la persona {i+1} (en metros): "))
    suma_alturas += altura

promedio_alturas = suma_alturas / n

print("El promedio de las alturas de las personas es:", promedio_alturas, "metros")
