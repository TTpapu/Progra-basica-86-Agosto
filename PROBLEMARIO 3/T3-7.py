numeros = input("Introduce una lista de números separados por comas: ")
lista_numeros = [float(num) for num in numeros.split(",")]
suma = sum(lista_numeros)
print(f"La suma de los números es: {suma}")