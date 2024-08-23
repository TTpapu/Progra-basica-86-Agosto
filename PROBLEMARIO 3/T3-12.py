import random

numero_aleatorio = random.randint(1, 100)
adivinanza = None

while adivinanza != numero_aleatorio:
    adivinanza = int(input("Adivina el número (entre 1 y 100): "))
    if adivinanza < numero_aleatorio:
        print("El número es mayor.")
    elif adivinanza > numero_aleatorio:
        print("El número es menor.")
    else:
        print("¡Correcto!")
