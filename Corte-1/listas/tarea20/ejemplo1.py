# Solicitar una cadena, guardarla en una matriz y mostrarla al revez

cadena = input("Ingresa una cadena: ")

matriz = []

x = len(cadena)
while x > 0 :
    matriz.append(cadena[x-1])
    x-=1

print(matriz)