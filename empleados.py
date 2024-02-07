empleados_A = 0
empleados_B = 0
total_sueldos = 0

cantidad_empleados = int(input("Ingrese la cantidad de empleados: "))

for i in range(cantidad_empleados):
    sueldo = float(input(f"Ingrese el sueldo del empleado {i+1}: "))
    total_sueldos += sueldo
    
    if sueldo <= 3000000:
        empleados_A += 1
    else:
        empleados_B += 1

total_gasto_sueldos = total_sueldos

print("Cantidad de empleados que cobran entre $1.000.000 y $3.000.000:", empleados_A)
print("Cantidad de empleados que cobran más de $3.000.000:", empleados_B)
print("Total gastado en sueldos al personal: $", total_gasto_sueldos)