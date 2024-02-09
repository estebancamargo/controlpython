def bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
        return True
    else:
        return False        
            
def contar(inicio, fin):
    contador = 0
    for año in range(inicio, fin + 1):
        if bisiesto(año):
            contador += 1
    return contador

inicio = 2000
fin = 2024
cantidad = contar(inicio, fin)
print(f"Entre los años {inicio} y {fin} hay {cantidad} años bisiestos.")

