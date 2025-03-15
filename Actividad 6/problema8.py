def registro_puntajes():
    puntajes = {}
    while True:
        nombre = input("Ingrese el nombre del jugador o 'salir': ")
        if nombre.lower() == 'salir':
            break
        puntaje = int(input("Ingrese el puntaje: "))
        puntajes[nombre] = puntaje
    
    print("Puntajes registrados:")
    for jugador, puntaje in puntajes.items():
        print(jugador, " : ", puntaje)

registro_puntajes()
