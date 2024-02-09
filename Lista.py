tupla = (2,4,6)
fecha = (9,"Febrero",2024)

print(tupla)
print(fecha)

palabras = int(input("Cuantas palabras deseas agregar"))

if palabras < 1:
    print("No es valido")
else:
    lista= []
    for i in range(palabras):
        palabra = input(f"Escriba la palabra {i+1}: ")
        lista += [palabra]
    print (f"La lista creada es: {lista}")    