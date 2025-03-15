def diccionario_notas():
    estudiantes = {}
    while True:
        nombre = input("Ingrese el nombre del estudiante o 'salir': ")
        if nombre.lower() == 'salir':
            break
        notas = list(map(int, input("Ingrese las notas  separadas por espacios: ").split()))
        estudiantes[nombre] = notas
    
    print("\nNotas de los estudiantes:")
    for nombre, notas in estudiantes.items():
        promedio = sum(notas) / len(notas)
        print(nombre,": ", notas, "Promedio: ", promedio)

diccionario_notas()
