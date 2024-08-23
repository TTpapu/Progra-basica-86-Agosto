calificaciones = input("Introduce las calificaciones separadas por comas: ")
lista_calificaciones = [float(cal) for cal in calificaciones.split(",")]
promedio = sum(lista_calificaciones) / len(lista_calificaciones)
print(f"El promedio de las calificaciones es: {promedio:.2f}")
