"""
Evaluar las estaturas del curso
Pedir x cantidad de estaturas y mostrar la estatura promedio del curso
"""
suma = 0
x=0
while True:
    estatura = float(input("Ingresa la estatura del estudiante " + str(x+1) + ", escribe 0 para salir: "))
    if estatura == 0:
        break
    suma+=estatura
    x+=1

esta = suma/x

print("La estatura promedio del curso es de ",esta,"m")