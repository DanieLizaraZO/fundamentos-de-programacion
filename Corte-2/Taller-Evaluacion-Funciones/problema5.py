# Definimos la función
def calcular_promedio(lista_numeros):
    # Incializamos suma en 0
    suma = 0
    
    # Creamos un for para recorrer la lista y sumar cada uno de los elementos
    for i in lista_numeros:
        suma+=i
        
    # Calculamos el promedio    
    promedio = suma/len(lista_numeros)
    
    # Devolvemos el promedio
    return promedio

# Definimos una lista cualquiera
lista = [1,2,3,4,5,6,7,8,9,10]

# Imprimos el valor de calcular_promedio en función de lista
print(calcular_promedio(lista))