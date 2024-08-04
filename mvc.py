from controlador import EstudianteControlador

if __name__ == "__main__":
    controlador = EstudianteControlador()
    
    while True:
        print("\nMenu")
        print("1. Agregar Estudiantes")
        print("2. Mostrar Estudiantes")
        print("3. Mostrar Estudiante Mayor")
        print("4. Agregar Profesores")
        print("5. Mostrar Profesores")
        print("6. Último Profesor Ingresado")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            controlador.agregar_estudiante()
        elif opcion == "2":
            controlador.mostrar_estudiantes()
        elif opcion == "3":
            controlador.estudiante_mayor()
        elif opcion == "4":
            controlador.agregar_profesor()
        elif opcion == "5":
            controlador.mostrar_profesores()
        elif opcion == "6":
            controlador.ultimo_profesor_ingresado()
        elif opcion == "7":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

