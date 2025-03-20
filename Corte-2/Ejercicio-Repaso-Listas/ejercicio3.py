"""
3. Dadas dos listas paralelas, una con nombres de estudiantes y otra con sus calificaciones, ordénalas de mayor a menor calificación.
"""

nombres = ["Daniel","Ana","Mateo","José"]
calificaciones = [100,60,80,40]

paralela = list(zip(calificaciones,nombres))

ordenado = []

for i in range(len(paralela)):
    maximo = max(paralela)
    ordenado.append(maximo)
    paralela.remove(maximo)

print(ordenado)
