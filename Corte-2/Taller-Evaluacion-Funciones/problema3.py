# Definimos la función con el parametro de los celsius
def convertir_celsius_a_fahrenheit(celsius):
    
    # Aplicamos la formular de fahrenheit
    F = ((celsius*9)/5)+32
    
    # Devolvemos el resultado
    return F

# Imprimimos el resultado de convertir_celsius_a_fahrenheit en función de los grados
print(convertir_celsius_a_fahrenheit(10))