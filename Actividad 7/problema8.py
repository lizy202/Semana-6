def registro_estudiantes():
    estudiantes = []
    while True:
        nombre = input("Ingrese el nombre del estudiante o 'salir': ")
        if nombre.lower() == "salir":
            break
        asignaturas = {}
        while True:
            asignatura = input(f"Ingrese una asignatura para {nombre} o 'fin': ")
            if asignatura.lower() == "fin":
                break
            calificacion = float(input(f"Ingrese la calificación de {asignatura}: "))
            asignaturas[asignatura] = calificacion
        amigos = input("Ingrese los nombres de los amigos de este estudiante separados por comas: ").split(",")
        estudiante = {
            "nombre": nombre,
            "asignaturas": asignaturas,
            "amigos": amigos
        }
        estudiantes.append(estudiante)
    
    print("\nEstudiantes registrados:")
    for estudiante in estudiantes:
        print(f"\n{estudiante['nombre']}:")
        print("Asignaturas y calificaciones:", estudiante['asignaturas'])
        print("Amigos:", estudiante['amigos'])

registro_estudiantes()