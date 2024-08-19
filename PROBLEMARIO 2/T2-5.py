def binario_a_entero(binario):
    try:
        entero = int(binario, 2)  # Convertir de binario a entero
        return entero
    except ValueError:
        return "Entrada no válida. Asegúrate de que sea un número binario."

# Solicitar al usuario que ingrese un número binario
numero_binario = input("Introduce un número binario: ")
print("Número entero:", binario_a_entero(numero_binario))
