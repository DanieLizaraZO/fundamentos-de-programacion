"""
6)	Un alumno desea calcular su nota final
 en una materia. Dicha calificación se compone
   de lo siguiente:
60% Un examen.
20% Quices. 
15% Talleres.
5% Participación
Realizar un programa que lea las 4 notas
 y calcule la nota final.

"""

#Entrada de datos
examen = float(input("Ingrese su calificación del examen: "))
quices = float(input("Ingrese su nota en los quices: "))
Taller = float(input("ingrese su nota en los talleres: "))
participación = float(input("Ingrese su nota de participación: "))

#Operacion
resulExamen = (60*examen)/100
resulQuices = (20*quices)/100
resulTalleres = (15*Taller)/100
resulParticipacion = (5*participación)/100
notaTotal = resulExamen+resulQuices+resulTalleres+resulParticipacion

#Salida de datos
print("Tu nota total es de ",notaTotal)