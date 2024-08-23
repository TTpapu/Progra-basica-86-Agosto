import os

nombre_archivo = input("Introduce la ruta de acceso del archivo puede ser txt: ")

# Verifica si el archivo existe en el directorio actual
if os.path.isfile(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            print("Contenido del archivo:")
            print(contenido)
    except IOError:
        print("Error al leer el archivo.")
else:
    print(f"El archivo '{nombre_archivo}' no se encontró en el directorio actual.")
