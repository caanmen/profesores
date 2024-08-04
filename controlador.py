

from datetime import datetime
from modelo import EstudianteModelo
from vista import EstudianteVista

class EstudianteControlador:
    def __init__(self):
        self.modelo = EstudianteModelo()
        self.vista = EstudianteVista()

    def agregar_estudiante(self):
        nombre, fecha_nacimiento, carrera = self.vista.pedir_datos_estudiante()
        edad = self.calcular_edad(fecha_nacimiento)
        self.modelo.agregar_estudiante(nombre, edad, carrera)

    def mostrar_estudiantes(self):
        estudiantes = self.modelo.obtener_estudiantes()
        self.vista.mostrar_estudiantes(estudiantes)

    def calcular_edad(self, fecha_nacimiento):
        hoy = datetime.now().date()
        fecha_nac = datetime.strptime(fecha_nacimiento, "%d/%m/%Y").date()
        edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
        return edad

    def estudiante_mayor(self):
        estudiantes = self.modelo.obtener_estudiantes()
        if estudiantes:
            mayor = max(estudiantes, key=lambda estudiante: estudiante.edad)
            self.vista.mostrar_estudiante_mayor(mayor)
        else:
            self.vista.mostrar_mensaje("No hay estudiantes registrados.")
