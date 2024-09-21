from tareas import Tarea, agregar_tarea, eliminar_tarea, listar_tareas
from typing import List, Set, Tuple, Optional

def mostrar_menu() -> None:
    print("\nMenú:")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

def obtener_fecha_limite() -> Optional[Tuple[int, int, int]]:
    try:
        fecha_str = input("Ingresa la fecha límite (DD/MM/YYYY) o deja en blanco si no hay fecha: ")
        if fecha_str:
            dia, mes, año = map(int, fecha_str.split('/'))
            return (año, mes, dia)
        return None
    except ValueError:
        print("Fecha inválida. Usa el formato DD/MM/YYYY.")
        return None

def gestionar_tareas() -> None:
    tareas_list: List[Tarea] = []

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == '1':
            nombre = input("Ingresa el nombre de la tarea: ")
            categoria = input("Ingresa la categoría de la tarea: ")
            etiquetas_str = input("Ingresa etiquetas separadas por comas: ")
            etiquetas = set(tag.strip() for tag in etiquetas_str.split(','))
            fecha_limite = obtener_fecha_limite()
            agregar_tarea(tareas_list, nombre, categoria, etiquetas, fecha_limite)
        elif opcion == '2':
            listar_tareas(tareas_list)
        elif opcion == '3':
            nombre = input("Ingresa el nombre de la tarea a eliminar: ")
            eliminar_tarea(tareas_list, nombre)
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción entre 1 y 4.")

if __name__ == "__main__":
    gestionar_tareas()