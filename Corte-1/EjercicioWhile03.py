"""
Solicitar n cantidad de sueltos y mostrar la sumatoria
de los mayores al mínimo
y la sumatoria de los menores o igual al mínimo
"""

salarioMinimo = 1400000

sumatoriaMax = 0
sumatoriaMin = 0
while True:

    n = int(input("Ingrese su salario: "))

    if n == 0:
        break
    elif n > salarioMinimo:
        sumatoriaMax+=n
    else:
        sumatoriaMin+=n

print("La sumatoria de los salarios más altos es de ",sumatoriaMax)
print("La sumatoria de los salarios más bajos o iguales es de ",sumatoriaMin)


