lista = []
valor = int(input("Ingrese el valor 0 para finalizar: "))

while valor != 0:
    lista.append(valor)
    valor=int(input("Ingrese un valor: "))

print("Tamaño de la lista",len(lista))

print(lista)