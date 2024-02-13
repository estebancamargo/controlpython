Persona = {
    "Nombre":"Julian Esteban",
    "Apellido":"Camargo Cuadrado",
    "Estatura":1.70,
    "Edad":18,
    "Email":"camargoesteban30@gmail.com",
    "CiudadNac":"Bogotá",
    "Genero":["Femenino","Masculino", "Otro"]
}
print(Persona)
#mostrar un elemento del diccionario
print(f"El nombre de la persona es:", {Persona["Nombre"]})

#agregar elemento del diccionario
Persona["Telefono"]=3015961747
print(Persona)
#Modificar valor del elemento del diccionario
Persona["Telefono"]=3138197630
print(Persona)
#Modificar la clave del elemento
Persona["Celular"]=Persona.pop("Telefono")
print(Persona)
#Eliminar un elemento del diccinario
del Persona["Celular"]
print(Persona)

#Iterar los item de las claves y valores
for clave,valor in Persona.items():
    print(clave , ": ",valor)