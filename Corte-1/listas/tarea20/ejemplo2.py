# Suma todos los elementos de una matriz

num = int(input("Ingresa cuantos número quieres en tu matriz: "))

matriz = []

for i in range(num):
    num2 = int(input("Ingresa: "))
    matriz.append(num2)

suma = 0

for i in matriz:
    suma+=i

print(f"La suma de los números de tu matriz es de {suma}")