def calcular_edad(ano_nacimiento, ano_actual):
    return ano_actual - ano_nacimiento

def main():
    # Solicitar el año en curso
    try:
        ano_actual = int(input("Introduce el año en curso: "))
    except ValueError:
        print("Por favor, ingresa un año válido.")
        return

    # Solicitar información de tres personas
    personas = []
    for i in range(3):
        nombre = input(f"Introduce el nombre de la persona {i+1}: ")
        try:
            ano_nacimiento = int(input(f"Introduce el año de nacimiento de {nombre}: "))
        except ValueError:
            print(f"El año de nacimiento de {nombre} no es válido. Debe ser un número entero.")
            return
        
        # Calcular la edad y agregar a la lista de personas
        edad = calcular_edad(ano_nacimiento, ano_actual)
        personas.append((nombre, edad))

    # Imprimir las edades
    print("\nEdad de las personas en el año en curso:")
    for nombre, edad in personas:
        print(f"{nombre} cumplirá {edad} años en {ano_actual}.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
