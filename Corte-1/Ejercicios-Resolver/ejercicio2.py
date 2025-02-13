"""
Un candidato a un empleo, realiza un test de capacitación, se obtuvo la siguiente
 información: cantidad total de preguntas que se le realizaron y la cantidad de preguntas
   que contestó correctamente. Se pide confeccionar un programa que ingrese los dos datos
     por teclado e informe el nivel del mismo según el porcentaje de respuestas correctas
     que ha obtenido, y sabiendo que:

Nivel máximo: Porcentaje>=95%.
Nivel medio: Porcentaje>=80% y <95%.
Nivel regular: Porcentaje>=60% y <80%.
Fuera de nivel: Porcentaje<60%.
"""

preguntas = int(input("Ingrese la cantidad de preguntas que se realizaron: "))
correct = int(input("Ingrese las preguntas que realizó correctamente: "))

porcentaje = (correct*100)/preguntas

if porcentaje >= 95:
    print("Ha obtenido el nivel máximo")
elif porcentaje >= 80:
    print("Ha obtenido el nivel medio")
elif porcentaje >= 60:
    print("Ha obtenido el nivel regular")
else:
    print("Estás fuera de nivel")