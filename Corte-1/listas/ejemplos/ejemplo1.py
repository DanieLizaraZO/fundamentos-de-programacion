num = int(input("Ingrese la cantidad de datos que desea ingresar: "))
lista = []
for i in range(num):
    numeros = int(input(f"Ingrese el número {i+1}: "))
    lista.append(numeros)

print(lista)