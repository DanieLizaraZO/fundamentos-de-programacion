"""
Desarrolla un programa en Python que permita gestionar las notas de un grupo de estudiantes.
El programa debe:

solicitar al usuario el número de estudiantes a registrar.
También debe cargar por teclado dos listas paralelas:

Una con los nombres de los estudaintes

otra con sus notas(valor entre 0 y 100).

deberá ordenar las listas de mayor a menor nota.

mostrar los estudiantes ordenados según su nota, indicando quién obtuvo la nota más alta y la más baja.

calcular el promedio de notas e indicar qué estudiantes están por encima y por debajo del promedio.
"""

numEstudiantes = int(input("Ingresa el número de estudiantes a registrar: "))
nombresEstudiantes = []
notasEstudiantes = []
for i in range(numEstudiantes):
    estudiante = input("Ingrese el nombre del estudiante: ")
    nota = int(input("Ingrese la nota del estudiante: "))
    nombresEstudiantes.append(estudiante)
    notasEstudiantes.append(nota)

paralela =  list(zip(notasEstudiantes,nombresEstudiantes))

ordenado = []
print(paralela)
for i in range(len(paralela)):
    maximo = max(paralela)
    ordenado.append(maximo)
    paralela.remove(maximo)

print(ordenado)

print(f"El estudiante con la nota mas alta fue {ordenado[0]}")
print(f"El estudiante con la nota más baja fue {ordenado[-1]}")

