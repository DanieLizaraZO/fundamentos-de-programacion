nombres = []
edades = []

for x in range(5):
    nom = input("Ingrese un nombre: ")
    nombres.append(nom)
    ed = int(input("Ingrese una edad: "))
    edades.append(ed)

print("Nombres de las personas mayores de edad")
for x in range(5):
    if edades[x] >= 18:
        print(nombres[x])