#Solicitar una cadena de caracteres y decir cuantos espacios en blanco tiene

cadena = input("Ingrese una cadena: ")

contador = 0
x = 0
while x < len(cadena):
    if cadena[x] == " ":
        contador+=1
    x+=1
if contador == 0:
    print("No tiene espacios en blanco")
else:
    print(f"Tiene {contador} espacios")