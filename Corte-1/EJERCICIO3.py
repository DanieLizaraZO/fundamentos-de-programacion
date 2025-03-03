#Solicitar por teclado una clave y evaluar que la clave tenga entre 10 y 20 caracteres para decir que es clave valida

clave = input("Ingrese su clave: ")

if len(clave) >= 10 and len(clave) <= 20:
    print("La clave es valida")
else:
    print("No es válida la clave")