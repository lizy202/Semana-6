def agenda_contactos():
    agenda = {}
    while True:
        accion = input("¿Qué desea hacer? \n 1-agregar \n 2-buscar \n 3-eliminar \n 4-salir ").lower()
        
        if accion == "salir":
            break
        elif accion == "agregar":
            nombre = input("Nombre del contacto: ")
            telefono = input("Número de teléfono: ")
            agenda[nombre] = telefono
        elif accion == "buscar":
            nombre = input("Nombre del contacto a buscar: ")
            if nombre in agenda:
                print(f"Teléfono de {nombre}: {agenda[nombre]}")
            else:
                print("Contacto no encontrado.")
        elif accion == "eliminar":
            nombre = input("Nombre del contacto a eliminar: ")
            if nombre in agenda:
                del agenda[nombre]
                print("Contacto ", nombre, " eliminado.")
            else:
                print("Contacto no encontrado.")
        else:
            print("Acción no válida.")

    print("Agenda de Contactos:")
    for nombre, telefono in agenda.items():
        print(f"{nombre}: {telefono}")

agenda_contactos()
