from datetime import datetime

fecha_nacimiento = input("Introduce tu fecha de nacimiento (YYYY-MM-DD): ")
fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
hoy = datetime.now()
dias_pasados = (hoy - fecha_nacimiento).days

print(f"Han pasado {dias_pasados} días desde tu nacimiento felicidades papu Bv200.")
