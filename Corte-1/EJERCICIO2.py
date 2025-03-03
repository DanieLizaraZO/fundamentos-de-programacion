# Solicitar una cadena de caracteres y mostrar la cantidad de vocales que tiene
cadena = input("Ingrese su cadena: ")
cadena = cadena.lower()
contador = 0
x = 0
while x < len(cadena):
    if cadena[x] == "a" or cadena[x] == "e" or cadena[x] == "i" or cadena[x] == "o" or cadena[x] == "u":
        contador+=1
    x+=1

if contador == 0:
    print("No tiene vocales")
else:
    print(f"Tiene {contador} vocales")