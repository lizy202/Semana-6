def registro_alumnos():
    alumnos = []
    while True:
        nombre = input("Ingrese el nombre del alumno o 'salir':")
        if nombre.lower() == "salir":
            break
        edad = int(input("Ingrese la edad: "))
        calificaciones = list(map(int, input("Ingrese las calificaciones separadas por espacios: ").split()))
        alumno = (nombre, edad, calificaciones)
        alumnos.append(alumno)
    
    print("\nLista de alumnos:")
    for alumno in alumnos:
        print("Nombre: ", alumno[0], "Edad: ",alumno[1], "Calificaciones: ",alumno[2])

registro_alumnos()
