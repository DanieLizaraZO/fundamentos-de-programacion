# Este es un breve ejemplo de la sintaxis del for para imprimir los números del 1 al 100 y determinando si son primos o no

for i in range(1,101):
    if i == 2 or i == 3 or i == 5 or i == 7:
        print(f'El número {i} es primo')
    elif i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        print(f'El número {i} no es primo')
    else:
        print(f'El número {i} es primo')