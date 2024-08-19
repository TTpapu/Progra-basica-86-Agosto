def filtrar_palabras(palabras, n):
    # Usamos una lista por comprensión para filtrar las palabras que tienen más de n caracteres
    palabras_filtradas = [palabra for palabra in palabras if len(palabra) > n]
    return palabras_filtradas

lista_palabras = input("Introduce las palabras separadas por espacios: ").split()
n = int(input("Introduce el número de caracteres: "))
resultado = filtrar_palabras(lista_palabras, n)
print("Las palabras con más de", n, "caracteres son:", resultado)