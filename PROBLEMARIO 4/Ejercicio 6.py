def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide el arreglo en dos mitades
    medio = len(arr) // 2
    izquierda = merge_sort(arr[:medio])
    derecha = merge_sort(arr[medio:])

    # Combina las dos mitades ordenadas
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    # Combina los elementos de manera ordenada
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agrega cualquier elemento restante
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    
    return resultado
print(merge_sort([3, 1, 4, 18, 5, 9]))