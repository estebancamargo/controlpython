def ingresar():
    enteros = []
    
    for x in range(5):
        Numero = int(input("Ingresar el numero"))
        enteros.append(Numero)
    imprimir(enteros)   
    sumar(enteros) 
        
def imprimir(enteros):

    print("Los datos de la lista son")
    for x in enteros:
        print(x)

def sumar(enteros):
    acum=0
    for x in enteros:
        acum=acum+x
    print("La suma de los numeros es: ",acum)    
ingresar()