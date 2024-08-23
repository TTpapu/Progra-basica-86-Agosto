def contar_palabras(oracion):
    oracion = oracion.strip()
    if not oracion:
        return 0
    palabras = oracion.split()
    cantidad_palabras = len(palabras)
    return cantidad_palabras

oracion = input("Introduce una oración: ")
cantidad_palabras = contar_palabras(oracion)
print(f"La oración tiene {cantidad_palabras} palabras.")
