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

class Profesor:
    def __init__(self, nombre, edad, materia):
        self.nombre = nombre
        self.edad = edad
        self.materia = materia

class ProfesorModelo:
    def __init__(self):
        self.profesores = []

    def agregar_profesor(self, nombre, edad, materia):
        profesor = Profesor(nombre, edad, materia)
        self.profesores.append(profesor)

    def obtener_profesores(self):
        return self.profesores
