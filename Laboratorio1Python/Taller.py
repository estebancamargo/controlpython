import random

def ejercicio1():
    print("Álvaro y Bárbara tiran un dado cada uno. El que saque el valor más alto, gana.")

    print("Presiona Enter para tirar el dado de Álvaro")
    input()
    alvaro = random.randint(1, 6)

    print("Presiona Enter para tirar el dado de Bárbara")
    input()
    barbara = random.randint(1, 6)

    print(f"Álvaro sacó: {alvaro}")
    print(f"Bárbara sacó: {barbara}")

    if alvaro > barbara:
        print("Gano Álvaro")
    elif barbara > alvaro:
        print("Gano Bárbara")
    else:
        print("Empate")

def ejercicio2():
        nombre = input("Ingrese su nombre: ")
        sexo = input("Ingrese su sexo (M/F): ")

        if sexo.upper() == "F":
           if nombre[0].upper() < "M":
            grupo = "A"
           else:
            grupo = "B"
        elif sexo.upper() == "M":
           if nombre[0].upper() > "N":
            grupo = "A"
           else:
            grupo = "B"
        print(f"Usted pertenece al grupo {grupo}")


def ejercicio3():
    edad = int(input("Ingrese la edad del cliente: "))

    if edad < 4:
      precio = 0
      print("El cliente puede entrar gratis.")
    elif 4 <= edad <= 18:
      precio = 30000
      print("El precio de la entrada es: ", precio)
    else:
      precio = 50000
    print("El precio de la entrada es: ", precio)
    print("Ejercicio 3")

def ejercicio4():
    contraseña_correcta = "Bogota"  

    while True:
       contraseña_ingresada = input("Ingrese la contraseña: ")
    
       if contraseña_ingresada == contraseña_correcta:
           print("Contraseña correcta")
           break
       else:
            print("Contraseña incorrecta. Inténtelo nuevamente.")
    


  
def ejercicio5():
    def calcular_total(cantidad, porcentaje=21):
        total = cantidad* (1 + porcentaje / 100)
        return total   

    cantidad = float(input("Ingrese la cantidad sin IVA: "))
    porcentaje = float(input("Ingrese el porcentaje de IVA: ") or 21)

    total = calcular_total(cantidad, porcentaje)
    print("Total con IVA:", total)

 
def ejercicio6():
    lista = []

    while True:
        print("1- Añadir número al final")
        print("2- Añadir número en una posición")
        print("3- Longitud de la lista")
        print("4- Eliminar último número")
        print("5- Eliminar número en posición") 
        print("6- Contar números")
        print("7- Posiciones de un número")
        print("8- Mostrar números")
        print("9- Salir")
    
        opcion = int(input("Ingrese una opción: "))
    
        if opcion == 1:
            n = int(input("Ingrese número a añadir: "))
            lista.append(n)
        
        elif opcion == 2:
           n = int(input("Ingrese número a insertar: "))
           pos = int(input("Ingrese posición: "))
           if 0 < pos <= len(lista):
              lista.insert(pos-1, n)
           else:
               print("Posición no válida")
        
        elif opcion == 3: 
            print("Longitud de la lista:", len(lista))
        
        elif opcion == 4:
           if lista: 
              print("Último número:", lista.pop())
           else:
              print("La lista está vacía")
        
        elif opcion == 5:
            pos = int(input("Ingrese posición a eliminar: "))
            if 0 < pos <= len(lista):
                print("Número eliminado:", lista.pop(pos-1)) 
            else:
                print("Posición no válida")
            
        elif opcion == 6:
            n = int(input("Ingrese número a contar: "))
            print(lista.count(n))
        
        elif opcion == 7:
            n = int(input("Ingrese número a buscar: "))
            posiciones = [i+1 for i, x in enumerate(lista) if x == n]
            print(posiciones)
        
        elif opcion == 8:
            print(lista)
        
        elif opcion == 9:
           break
        
        else:
             print("Opción inválida")

    print("Programa finalizado")

def ejercicio7():
    precios = {
      "Manzana": 1500,
      "Pera": 2000,  
      "Banano": 500,
      "Naranja": 450
    }

    continuar = "si"

    while continuar.lower() == "si":
      fruta = input("Nombre de la fruta: ")
  
      cantidad = int(input("Cantidad vendida: "))
  
      if fruta in precios:
        precio_unidad = precios[fruta]
        print(f"Total para {cantidad} {fruta}(s): {round(cantidad * precio_unidad, 2)}")  
      else:
        print("Fruta no existe en el diccionario de precios")
    
      continuar = input("¿Desea consultar otro precio (Si/No)? ")
  
    print("Fin de la consulta")

 
def ejercicio8():
    
   cesta = {}
   total = 0

   while True:
       articulo = input("Introduzca el artículo (FIN para salir): ")
       if articulo.upper() == "FIN":
          break
        
       precio = float(input("Precio del artículo: "))
       cesta[articulo] = precio
       total += precio

   print("\nLista de la compra:")
   for articulo, precio in cesta.items():
       print(f"{articulo}: {precio:}")
     
   print(f"\nTotal: {total:}")
 
def ejercicio9():
    alumnos = {}

    num_alumnos = int(input("Número de alumnos: "))

    for _ in range(num_alumnos):
       nombre = input("Nombre del alumno: ")
    
       if nombre in alumnos:
           print("Nombre de alumno ya existe")
           continue  
        
       notas = [] 
       nota = 0
    
       while nota >= 0:
           nota = float(input("Nota (numero negativo para terminar): "))
           if nota >= 0:
               notas.append(nota)
            
       alumnos[nombre] = notas
    
    print()        
    for nombre, notas in alumnos.items():
        suma = sum(notas)
        num_notas = len(notas)
    
        total = suma / num_notas
    
        print(f"{nombre}: {total:}")
 
 
def mostrar_menu():
    print("Menú principal")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("6. Ejercicio 6")
    print("7. Ejercicio 7")
    print("8. Ejercicio 8")
    print("9. Ejercicio 9")
    print("10. Salir")

def principal():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio2()
        elif opcion == "3":
            ejercicio3()
        elif opcion == "4":
            ejercicio4()  
        elif opcion == "5":
            ejercicio5()  
        elif opcion == "6":
            ejercicio6()  
        elif opcion == "7":
            ejercicio7()  
        elif opcion == "8":
            ejercicio8()  
        elif opcion == "9":
            ejercicio9()                        
        elif opcion == "10":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")

principal()