def contar_mayusculas(cadena):
    conteo = sum(1 for c in cadena if c.isupper())
    return conteo

# Solicitar al usuario que ingrese una cadena
cadena_usuario = input("Introduce una cadena: ")
print("Número de letras mayúsculas:", contar_mayusculas(cadena_usuario))
