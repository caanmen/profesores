class EstudianteVista:
    def mostrar_estudiantes(self, estudiantes):
        print("Lista de Estudiantes:")
        for estudiante in estudiantes:
            print(f"Nombre: {estudiante.nombre}, Edad: {estudiante.edad}, Carrera: {estudiante.carrera}")

    def pedir_datos_estudiante(self):
        nombre = input("Ingrese el nombre del estudiante: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento (dd/mm/yyyy): ")
        carrera = input("Ingrese la carrera del estudiante: ")
        return nombre, fecha_nacimiento, carrera
    
    def mostrar_estudiante_mayor(self, estudiante):
        print(f"El estudiante mayor es {estudiante.nombre} con {estudiante.edad} años.")

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

class ProfesorVista:
    def mostrar_profesores(self, profesores):
        print("Lista de Profesores:")
        for profesor in profesores:
            print(f"Nombre: {profesor[0]}, Edad: {profesor[1]}, Materia: {profesor[2]}")

    def pedir_datos_profesor(self):
        nombre = input("Ingrese el nombre del profesor: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento (dd/mm/yyyy): ")
        materia = input("Ingrese la materia que enseña: ")
        return nombre, fecha_nacimiento, materia
    
    def mostrar_profesor(self, profesor):
        print(f"Último profesor ingresado es {profesor[0]} con {profesor[1]} años, y enseña {profesor[2]}.")

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
