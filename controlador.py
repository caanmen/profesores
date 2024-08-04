from datetime import datetime
from modelo import EstudianteModelo, ProfesorModelo  # Importar el modelo del profesor
from vista import EstudianteVista, ProfesorVista  # Importar la vista del profesor

class EstudianteControlador:
    def __init__(self):
        self.modelo_estudiantes = EstudianteModelo()
        self.modelo_profesores = ProfesorModelo()  # Instanciar el modelo del profesor
        self.vista_estudiantes = EstudianteVista()
        self.vista_profesores = ProfesorVista()  # Instanciar la vista del profesor
        self.pila_profesores = []

    def agregar_estudiante(self):
        nombre, fecha_nacimiento, carrera = self.vista_estudiantes.pedir_datos_estudiante()
        edad = self.calcular_edad(fecha_nacimiento)
        self.modelo_estudiantes.agregar_estudiante(nombre, edad, carrera)

    def mostrar_estudiantes(self):
        estudiantes = self.modelo_estudiantes.obtener_estudiantes()
        self.vista_estudiantes.mostrar_estudiantes(estudiantes)

    def estudiante_mayor(self):
        estudiantes = self.modelo_estudiantes.obtener_estudiantes()
        if estudiantes:
            mayor = max(estudiantes, key=lambda estudiante: estudiante.edad)
            self.vista_estudiantes.mostrar_estudiante_mayor(mayor)
        else:
            self.vista_estudiantes.mostrar_mensaje("No hay estudiantes registrados.")

    def agregar_profesor(self):
        nombre, fecha_nacimiento, materia = self.vista_profesores.pedir_datos_profesor()
        edad = self.calcular_edad(fecha_nacimiento)
        self.modelo_profesores.agregar_profesor(nombre, edad, materia)
        self.pila_profesores.append((nombre, edad, materia))

    def mostrar_profesores(self):
        profesores = self.modelo_profesores.obtener_profesores()
        self.vista_profesores.mostrar_profesores(profesores)

    def ultimo_profesor_ingresado(self):
        if self.pila_profesores:
            profesor = self.pila_profesores[-1]
            self.vista_profesores.mostrar_profesor(profesor)
        else:
            self.vista_profesores.mostrar_mensaje("No hay profesores registrados.")

    def calcular_edad(self, fecha_nacimiento):
        hoy = datetime.now().date()
        fecha_nac = datetime.strptime(fecha_nacimiento, "%d/%m/%Y").date()
        edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
        return edad
