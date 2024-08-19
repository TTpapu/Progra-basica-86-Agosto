def contar_nombres_por_letra(nombres, letra):
    return sum(1 for nombre in nombres if nombre.lower().startswith(letra.lower()))

# Solicitar al usuario que ingrese una lista de nombres
nombres = input("Introduce los nombres separados por espacios: ").split()

# Solicitar al usuario la letra a buscar
letra = input("Introduce la letra a buscar: ")
print(f"Cantidad de nombres que comienzan con '{letra}':", contar_nombres_por_letra(nombres, letra))
