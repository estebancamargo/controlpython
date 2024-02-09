texto = "Buenos dias definiendo un parametro en una funcion"

def mensaje():
    N1 = int(input("Ingresar el primer numero"))
    N2 = int(input("Ingresar el segundo numero"))
    calcularmayor(N1,N2)
    positivo(N1,N2)
    
def calcularmayor(num1,num2):    
    if num1>num2:
        print("El primer numero es el mayor")
    elif num1==num2:
        print("Son numeros iguales")
    else: 
        print("El segundo numero es el mayor")


def positivo(p1,p2):
    if p1>0 and p2>0:
        print("Son numeros positivos")
    
    elif p1<0 and p2<0:
        print("Son negativos")    
    else:
        print("Al menos uno de los numeros no es positivo")            
            
            
mensaje()    
