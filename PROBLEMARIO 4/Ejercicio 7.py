def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Elegir el pivote (puede ser el último elemento)
    pivote = arr[-1]
    izquierda = [x for x in arr[:-1] if x <= pivote]
    derecha = [x for x in arr[:-1] if x > pivote]

    # Recursión
    return quick_sort(izquierda) + [pivote] + quick_sort(derecha)
print(quick_sort([7, 1, 3, 8, 5, 9]))