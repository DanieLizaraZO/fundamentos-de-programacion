cantidadInvertir = int(input("Ingrese una cantidad a invertir: "))
intetesAnual = int(input("Ingrese el interes anual: "))
numeroAnos = int(input("Ingrese el número de años: "))

capitalObtenido = ((cantidadInvertir*intetesAnual)/100)*numeroAnos
capitalTotal = capitalObtenido+cantidadInvertir
print("El capital obtenido es de ",capitalObtenido)