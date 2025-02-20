"""
1)	Escribir un programa que le pregunte al
 usuario que edad tiene y de acuerdo con la edad
  y muestre por pantalla lo siguiente:
	0 – 5 años, Primera Infancia.
	6 – 11 años, Infancia.
	12 –18 años, Adolescencia.
	19 - 26 años, Juventud.
	27- 59 años, Adultez.
	 >= 60 años, Vejez.

"""
#Entrada de datos
edad = int(input("Ingrese su edad: "))

#Condicional y salida de datos
if edad >= 0:
    if edad >= 0 and edad <= 5:
        print("Estás en la primera infancia")
    elif edad >= 6 and edad <= 11:
        print("Estás en la infancia")
    elif edad >= 12 and edad <= 18:
        print("Estás en la adolecencia")
    elif edad >= 19 and edad <= 26:
        print("Estás en la juventud")
    elif edad >= 27 and edad <= 59:
        print("Estás en la adultez")
    else:
        print("Estás en la vejez")
else:
    print("Edad no válida")





