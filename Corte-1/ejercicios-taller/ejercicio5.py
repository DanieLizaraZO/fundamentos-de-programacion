"""
7)	Una tienda de fruta desea conocer el valor a cobrar de la venta de una fruta,
 para ello se debe realizar un programa que solicite el valor del kilo y el peso
   de la fruta a vender, se debe calcular el valor a cobrar por la venta ejemplo:
     el precio es 1000 por kilo y se va a comprar 5 kilos el valor a pagar 5.000.
"""

#Entrada de datos
valorKilo = float(input("Ingrese el costo del kilo: "))
peso= float(input("Ingrese el peso de la fruta en kilos: "))

#Operacion
precio = valorKilo*peso

#Salida de datos
print("El precio de la fruta es de ",precio," pesos")