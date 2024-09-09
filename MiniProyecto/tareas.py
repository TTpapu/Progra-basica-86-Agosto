from typing import List, Set, Tuple, Optional

class Tarea:
    def __init__(self, nombre: str, categoria: str, etiquetas: Set[str], fecha_limite: Optional[Tuple[int, int, int]] = None):
        self.nombre = nombre
        self.categoria = categoria
        self.etiquetas = etiquetas
        self.fecha_limite = fecha_limite

    def __str__(self) -> str:
        fecha = f"{self.fecha_limite[2]:02d}/{self.fecha_limite[1]:02d}/{self.fecha_limite[0]}" if self.fecha_limite else "Sin fecha límite"
        return f"Tarea: {self.nombre}\nCategoría: {self.categoria}\nEtiquetas: {', '.join(self.etiquetas)}\nFecha límite: {fecha}"

def agregar_tarea(tareas: List[Tarea], nombre: str, categoria: str, etiquetas: Set[str], fecha_limite: Optional[Tuple[int, int, int]] = None) -> None:
    tarea = Tarea(nombre, categoria, etiquetas, fecha_limite)
    tareas.append(tarea)
    print(f"Tarea '{nombre}' agregada.")

def eliminar_tarea(tareas: List[Tarea], nombre: str) -> None:
    for tarea in tareas:
        if tarea.nombre == nombre:
            tareas.remove(tarea)
            print(f"Tarea '{nombre}' eliminada.")
            return
    print(f"Tarea '{nombre}' no encontrada.")

def listar_tareas(tareas: List[Tarea]) -> None:
    if not tareas:
        print("No hay tareas.")
    else:
        for tarea in tareas:
            print(tarea)
            print("-" * 20)