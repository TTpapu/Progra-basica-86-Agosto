def potencia_matriz(matriz, exponente):
    if exponente == 0:
        # Devuelve la matriz identidad
        return [[1 if i == j else 0 for j in range(len(matriz))] for i in range(len(matriz))]
    
    if exponente == 1:
        return matriz

    # Divide el problema
    mitad = exponente // 2
    mitad_potencia = potencia_matriz(matriz, mitad)

    # Multiplica la matriz por sí misma
    resultado = multiplicar_matrices(mitad_potencia, mitad_potencia)

    # Si el exponente es impar, multiplica por la matriz original
    if exponente % 2 == 1:
        resultado = multiplicar_matrices(resultado, matriz)

    return resultado

def multiplicar_matrices(A, B):
    # Suponiendo que A y B son matrices cuadradas de tamaño n x n
    n = len(A)
    resultado = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                resultado[i][j] += A[i][k] * B[k][j]

    return resultado
M = [[1, 2], [3, 4]]
print(potencia_matriz(M, 2))