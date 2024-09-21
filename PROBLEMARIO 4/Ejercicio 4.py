def potencia(a, b):
    # Caso base
    if b == 0:
        return 1
    # Recursión
    return a * potencia(a, b - 1)
print (potencia(4, 9))