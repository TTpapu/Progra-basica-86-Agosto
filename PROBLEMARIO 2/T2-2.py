def mas_larga(palabras):
    if not palabras:
        raise ValueError("La lista está vacía. Proporcione una lista con al menos una palabra.")
    
    # Inicializamos la palabra más larga con el primer elemento de la lista
    palabra_larga = palabras[0]
    
    # Checamos sobre el resto de las palabras para encontrar la más larga
    for palabra in palabras[1:]:
        if len(palabra) > len(palabra_larga):
            palabra_larga = palabra
    
    return palabra_larga

lista_palabras = input("Introduce las palabras separadas por espacios: ").split()
print("La palabra más larga es:", mas_larga(lista_palabras))