def contador_palabras(texto):
    palabras = texto.split()
    contador = {}
    for palabra in palabras:
        palabra = palabra.lower().strip(".,!?")
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    return contador

texto = "Esto no es una silumacion rendirse no es una opcion"
resultado = contador_palabras(texto)
for palabra, frecuencia in resultado.items():
    print(f"{palabra}: {frecuencia}")
