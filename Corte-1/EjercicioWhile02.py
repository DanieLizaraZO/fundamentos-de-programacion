"""
Solicitar x cantidad de números enteros y mostrar cuantos son pares
y cuantos son impares
"""
x = int(input("ingrese un numero :"))
contadorPar = 0
contadorImpar = 0
contador = 1
while  contador <= x:
    if contador%2==0:
        contadorPar +=1
    else:
        contadorImpar +=1
    contador=contador+1
print("los numeros pares son:",contadorPar)
print("los numeros impares son:",contadorImpar)