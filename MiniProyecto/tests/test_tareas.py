import unittest
from tareas import Tarea, agregar_tarea, eliminar_tarea, listar_tareas
from typing import List, Set, Tuple

class TestTareas(unittest.TestCase):

    def setUp(self):
        self.tareas_list = []

    def test_agregar_tarea(self):
        agregar_tarea(self.tareas_list, "Tarea 1", "Personal", {"importante"}, (2024, 12, 25))
        self.assertEqual(len(self.tareas_list), 1)
        self.assertEqual(self.tareas_list[0].nombre, "Tarea 1")

    def test_eliminar_tarea(self):
        agregar_tarea(self.tareas_list, "Tarea 2", "Trabajo", {"urgente"}, None)
        eliminar_tarea(self.tareas_list, "Tarea 2")
        self.assertEqual(len(self.tareas_list), 0)

    def test_listar_tareas(self):
        agregar_tarea(self.tareas_list, "Tarea 3", "Estudio", {"media"}, (2024, 9, 9))
        import io
        import sys
        output = io.StringIO()
        sys.stdout = output
        listar_tareas(self.tareas_list)
        sys.stdout = sys.__stdout__
        self.assertIn("Tarea: Tarea 3", output.getvalue())

if __name__ == "__main__":
    unittest.main()