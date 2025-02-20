"""
2)	Escribir un programa que solicite dos
 números y muestre por pantalla su división.
   Si el resultado es cero el programa debe
     mostrar un error.
Ejemplo:  2 / 4 = 0

"""
#Entrada de datos
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("ingrese el segundo número: "))

#Operacion
resul = num1/num2

#Condicional y salida de datos
if num2 == 0:
    print("No se puede realizar")
elif resul == int(0):
    print("Há habido un error, el resultado debe dar mayor a uno")
else:
    print("El resultado es ",resul)