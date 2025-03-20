"""
2. Dadas dos listas, una con nombres de productos y otra con sus respectivos precios, ordena ambas listas en función de los precios (de menor a mayor).
"""

productos = ["Laptop", "Mouse", "Teclado", "Monitor"]
precios = [800, 20, 50, 300]

paralela = list(zip(precios,productos))

ordenado = []

for i in range(len(paralela)):
    minimo = min(paralela)
    ordenado.append(minimo)
    paralela.remove(minimo)

print(ordenado)