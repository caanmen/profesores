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

