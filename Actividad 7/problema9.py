def agenda_contactos():
    contactos = []
    while True:
        accion = input("¿Qué desea hacer? \n 1-agregar \n 2-buscar \n 3-eliminar \n 4-salir: ").lower()
        
        if accion == "salir":
            break
        elif accion == "agregar":
            nombre = input("Nombre del contacto: ")
            telefono = input("Número de teléfono: ")
            correos = input("Correos electrónicos (separados por comas): ").split(",")
            contacto = {
                "nombre": nombre,
                "telefono": telefono,
                "correos": correos
            }
            contactos.append(contacto)
        elif accion == "buscar":
            nombre = input("Nombre del contacto a buscar: ")
            encontrado = False
            for contacto in contactos:
                if contacto["nombre"] == nombre:
                    print(f"Teléfono: {contacto['telefono']}, Correos: {', '.join(contacto['correos'])}")
                    encontrado = True
                    break
            if not encontrado:
                print("Contacto no encontrado.")
        elif accion == "eliminar":
            nombre = input("Nombre del contacto a eliminar: ")
            for contacto in contactos:
                if contacto["nombre"] == nombre:
                    contactos.remove(contacto)
                    print(f"Contacto {nombre} eliminado.")
                    break
            else:
                print("Contacto no encontrado.")
        else:
            print("Acción no válida.")

    print("Agenda de Contactos:")
    for contacto in contactos:
        print(f"{contacto['nombre']}: Teléfono: {contacto['telefono']}, Correos: {', '.join(contacto['correos'])}")

agenda_contactos()