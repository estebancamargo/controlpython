Edad = int(input("Por favor ingresar su edad"))

if Edad < 4:
    Ingreso = 0
elif Edad <=18:
    Ingreso = 5000
else:
    Ingreso = 10000
    
print("Precio de la entrada es ",Ingreso)        