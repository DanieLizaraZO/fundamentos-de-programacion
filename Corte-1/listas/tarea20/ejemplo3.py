# Encontrar los números primos de una Matriz e imprimir otra matriz con sus números primos

numeros = [15,45,65,12,11,101,201,654,224,1001,3001]

numPrimos = []

for i in numeros:
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        numPrimos.append(i)
    
print(numPrimos)