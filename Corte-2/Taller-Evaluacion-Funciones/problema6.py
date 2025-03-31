# Definimos la función con sus argumentos
def crear_mensaje(nombre, mensaje = "Bienvenido al curso"):
    
    #Devolvemos el valor (mensaje es un parametro que cambia o no dependiendo de si el usuario lo decide)
    return f"{nombre}, {mensaje}"
    
# Imprimimos la función de crear_mensaje pasandole solo el nombre
print(crear_mensaje("Daniel"))