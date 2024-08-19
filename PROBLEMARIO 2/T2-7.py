# Solicitar al usuario que ingrese las edades
edades = []
for i in range(10):
    try:
        edad = int(input(f"Introduce la edad de la persona {i+1}: "))
        edades.append(edad)
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Contar cuántas edades son mayores a 20
cantidad_mayores_20 = sum(1 for edad in edades if edad > 20)
print("Cantidad de personas con edades superiores a 20:", cantidad_mayores_20)
