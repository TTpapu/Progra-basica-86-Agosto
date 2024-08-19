def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

# Solicitar al usuario un año
ano_usuario = int(input("Introduce un año: "))
if es_bisiesto(ano_usuario):
    print(f"El año {ano_usuario} es bisiesto.")
else:
    print(f"El año {ano_usuario} no es bisiesto.")
