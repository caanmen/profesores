class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

class EstudianteModelo:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, nombre, edad, carrera):
        estudiante = Estudiante(nombre, edad, carrera)
        self.estudiantes.append(estudiante)

    def obtener_estudiantes(self):
        return self.estudiantes
