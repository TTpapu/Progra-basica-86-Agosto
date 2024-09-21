def invertir_cadena(cadena):
    # Caso base
    if cadena == "":
        return cadena
    # Recursión
    return cadena[-1] + invertir_cadena(cadena[:-1])
print(invertir_cadena('buuu'))