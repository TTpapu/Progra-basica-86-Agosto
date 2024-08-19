def contar_vocales(palabra):
    conteo_vocales = {vocal: palabra.lower().count(vocal) for vocal in "aeiou"}
    return conteo_vocales

# Solicitar al usuario una palabra
palabra_usuario = input("Introduce una palabra: ")
conteo = contar_vocales(palabra_usuario)
print("Conteo de vocales:", conteo)
