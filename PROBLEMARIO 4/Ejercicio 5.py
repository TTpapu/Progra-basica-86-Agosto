def suma_digitos(n):
    # Asegurarse de trabajar con el valor absoluto
    n = abs(n)
    
    # Caso base
    if n == 0:
        return 0
    
    # Recursión
    return n % 10 + suma_digitos(n // 10)
print(suma_digitos(421))