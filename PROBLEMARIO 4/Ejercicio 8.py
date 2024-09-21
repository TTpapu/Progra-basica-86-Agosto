def busqueda_binaria(lista, objetivo, izquierda=0, derecha=None):
    if derecha is None:
        derecha = len(lista) - 1

    if izquierda > derecha:
        return -1  # Elemento no encontrado

    medio = (izquierda + derecha) // 2

    if lista[medio] == objetivo:
        return medio
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, objetivo, medio + 1, derecha)
    else:
        return busqueda_binaria(lista, objetivo, izquierda, medio - 1)
print(busqueda_binaria([1, 2, 3, 4, 5], 3))