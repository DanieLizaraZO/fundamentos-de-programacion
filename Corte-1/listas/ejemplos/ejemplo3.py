nombres = []

numNombres = int(input("Cuantos nombres quieres ingresa? "))

for i in range(numNombres):
    nom = input("Ingresa nombre: ")
    nombres.append(nom)

print(nombres)