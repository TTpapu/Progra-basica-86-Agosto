peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))

imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc:.2f}")

if imc < 18.5:
    print("Estás en bajo peso.")
elif 18.5 <= imc < 24.9:
    print("Estás en un peso normal.")
elif 25 <= imc < 29.9:
    print("Estás en sobrepeso.")
else:
    print("Estás en obesidad.")
