def diccionario_sinonimos():
    sinonimos = {
        "feliz": ["contento", "alegre", "jovial"],
        "triste": ["melancólico", "deprimido", "afligido"],
        "rápido": ["veloz", "acelerado", "ágil"]
    }

    palabra = input("Ingresa una palabra para buscar su sinónimo: ")
    if palabra in sinonimos:
        print("Sinónimos de ", palabra,":",', '.join(sinonimos[palabra]))
    else:
        print("No se encontraron sinónimos.")
    
    print("Palabras disponibles en el diccionario:")
    for palabra in sinonimos.keys():
        print(palabra)


diccionario_sinonimos()
