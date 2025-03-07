# Queremos mostrar el promedio de las edades de los niños primaria
edades = [4,6,8,8,10,7,5,6,5,11]

# Bucle para sumar las edades
suma = 0
for i in edades:
    suma = suma + i

# Operación
promedio = suma/len(edades)

# Imprimir el promedio
print(f"El promedio de las edades de los niños de primaria es: {promedio} años")

