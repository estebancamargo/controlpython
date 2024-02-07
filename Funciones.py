def inicio():
    
    print("MENU PRINCIPAL")
    print("Seleccione la opcion correcta:")
    print("1. Operacion sumar")
    print("2. Operacion resta")
    print("3. Operacion multiplicar")
    print("4. Operacion dividir") 
def main():
    while True:
        inicio()
        opcion = int(input("Seleccione la opcion"))
        if opcion == 1:
           print("Ha seleccionado la suma")    
           Num1 = int(input("Ingresar el 1 numero"))
           Num2 = int(input("Ingresar el 2 numero"))
           sumar = Num1+Num2
           print("El resultado de la suma es: ",sumar)
        elif opcion == 2:
             print("Ha seleccionado la resta")
             Num1 = int(input("Ingresar el 1 numero"))
             Num2 = int(input("Ingresar el 2 numero"))
             restar = Num1-Num2
             print("El resultado de la suma es: ",restar)
        elif opcion == 3:
             print("Ha seleccionado operacion multiplicar")
        elif opcion == 4:
             print("Ha seleccionado operacion dividir") 
        elif opcion == 5:
             print("Hasta luego")
             break
        else:
             print("Opcion no valida, seleccione una opcion valida")    
                            
inicio()    
main()