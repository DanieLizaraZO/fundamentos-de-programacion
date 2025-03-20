"""
4. Dadas dos listas de números del mismo tamaño, suma los valores de ambas y almacena el resultado en una nueva lista.
"""

lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = [11,22,33,44,55,66,77,88,99,110]

suma = []

for i in range(len(lista1)):
    suma.append(lista1[i]+lista2[i])

print(suma)