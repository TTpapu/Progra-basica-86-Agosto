def fibonacci(n):
    # Caso base
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Recursión
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))