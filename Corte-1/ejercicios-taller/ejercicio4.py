"""
	Realizar un programa que resuelva la ecuación (x+y)^2
    , se debe solicitar el valor de X y Y, mostrar el resultado.
"""
#Entrada de datos
print("Este es un valor para resolver la ecuación (x+y)^2")

#Operacion
X = float(input("ingrese el valor de X: "))
Y = float(input("ingrese el valor de Y: "))

#Salida de datos
print("El resultado es ",(X*X) + (2*X*Y) + (Y*Y))