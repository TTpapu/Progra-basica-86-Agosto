def max_in_list(numbers):
    if not numbers:
        raise ValueError("La lista está vacía. Proporcione una lista con al menos un número.")
    
    # Inicializamos el valor máximo con el primer elemento de la lista
    max_value = numbers[0]
    
    # Iteramos sobre el resto de los elementos para encontrar el mayor
    for num in numbers[1:]:
        if num > max_value:
            max_value = num
    
    return max_value

numbers_list = [int(x) for x in input("Introduce los números separados por espacios: ").split()]
print("El número máximo es:", max_in_list(numbers_list))
