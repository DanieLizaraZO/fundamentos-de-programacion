"""1. Programa que permita cargar un número entero positivo
 de hasta cuatro cifras y muestre un mensaje indicando si tiene
 1, 2, 3 o 4 cifras. Mostrar un mensaje de error si el número de cifras es mayor."""

num = int(input("Ingrese un número entre 1 y 4 cifras: "))

if num>=10000 or num<0:
    print("El número debe ser positivo y no puede ser mayor de cuatro cifras")
elif num >= 1 and num<10:
    print("Su número tiene 1 cifra")
elif num >=10 and num<100:
    print("Su número tiene 2 cifras")
elif num >= 100 and num < 1000:
    print("Su número tiene 3 cifras")
else:
    print("Su número tiene 4 cifras")

