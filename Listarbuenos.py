#definir las listas
Nombres=[]
Notas=[]
Amejor=[]    
mb=0
b=0
iN=0

for x in range(1,4):
    Nom = input(f"Por favor ingresar el nombre del alumno {x} : ")
    Nombres.append(Nom)
    No = int(input(f"Por favor ingresar las notas del alumnos {x} : "))
    Notas.append(No)
    
    for y in range(len(Nombres)):
        print(Nombres[y])
        print(Notas[y])
    
    
    if Notas[y]>=8:
        print("Alumno muy bueno")
        mb += 1
        Amejor.append(Nombres[y])
    else:
        if Notas[y]>=4:
            print("Alumno bueno")
            b += 1
        else:
            print("Alumno no aprueba la materia")
            iN += 1
print("Listado inicial de los alumnos son: ",Nombres)            
            
eliminar = []            
for z in range(len(Notas)):
    if Notas[z]>=4 and Notas[z]<=7:
        #Notas.pop(z)
        #Nombres.pop(z
        eliminar.append(z)
for d in sorted(eliminar,reverse=True):
    Notas.pop[d]
    Nombres.pop[d]
            
        
        
print("Cantidad de alumnos muy buenos son: ",mb)   
print("Los Nombres De Los Mejores Alumnos x Nota Son: ",Amejor)
print("Listado de alumnos ",Nombres)
