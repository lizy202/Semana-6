def diccionario_traduccion():
    traducciones = {}
    while True:
        palabra = input("Ingrese la palabra en el idioma original o 'salir': ")
        if palabra.lower() == "salir":
            break
        traduccion = input("Ingrese la traducción de la palabra: ")
        traducciones[palabra] = traduccion
    
    print("\nTraducciones:")
    for palabra, traduccion in traducciones.items():
        print(palabra, "->", traduccion)

diccionario_traduccion()