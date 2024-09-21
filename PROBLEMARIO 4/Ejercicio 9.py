def multiplicar_matrices(A, B):
    # Asumiendo que las matrices A y B son cuadradas y de tamaño n x n
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Divide las matrices en cuartetos
    mid = n // 2
    A11 = [[A[i][j] for j in range(mid)] for i in range(mid)]
    A12 = [[A[i][j] for j in range(mid, n)] for i in range(mid)]
    A21 = [[A[i][j] for j in range(mid)] for i in range(mid, n)]
    A22 = [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]

    B11 = [[B[i][j] for j in range(mid)] for i in range(mid)]
    B12 = [[B[i][j] for j in range(mid, n)] for i in range(mid)]
    B21 = [[B[i][j] for j in range(mid)] for i in range(mid, n)]
    B22 = [[B[i][j] for j in range(mid, n)] for i in range(mid, n)]

    # Calcula los productos
    M1 = multiplicar_matrices(A11, B11)
    M2 = multiplicar_matrices(A12, B21)
    M3 = multiplicar_matrices(A11, B12)
    M4 = multiplicar_matrices(A12, B22)
    M5 = multiplicar_matrices(A21, B11)
    M6 = multiplicar_matrices(A22, B21)
    M7 = multiplicar_matrices(A21, B12)
    M8 = multiplicar_matrices(A22, B22)

    # Combina los resultados
    C11 = [[M1[i][0] + M2[i][0] for i in range(mid)]]
    C12 = [[M3[i][0] + M4[i][0] for i in range(mid)]]
    C21 = [[M5[i][0] + M6[i][0] for i in range(mid)]]
    C22 = [[M7[i][0] + M8[i][0] for i in range(mid)]]

    # Combina las partes en la matriz resultado
    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(multiplicar_matrices(A, B))