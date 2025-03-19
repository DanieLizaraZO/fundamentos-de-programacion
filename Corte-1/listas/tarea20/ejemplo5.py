# Cuenta los números pares que hay en una lista

numPares = [1,2,3,4,5,6,7,8,9,10]

suma = 0

for i in numPares:
    if i % 2 == 0:
        suma+=1
    
print(suma)