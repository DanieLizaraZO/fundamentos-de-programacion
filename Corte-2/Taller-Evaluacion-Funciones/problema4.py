# Definimos la función con sus parametros
def torres_de_hanoi(n, origen, destino, auxiliar):
    
    # Si solo hay un disco directamente pasamos de A a C
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return
    # Si hay más de un disco debemos empezar separando el más pequeño y luego el siguiente
    torres_de_hanoi(n - 1, origen, auxiliar, destino)
    print(f"Mover disco {n} de {origen} a {destino}")
    torres_de_hanoi(n - 1, auxiliar, destino, origen)

# Imprimimos el resultado de torres_de_hanoi cuando teenemos 2 discos
torres_de_hanoi(2, 'A', 'C', 'B')
