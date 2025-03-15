def palabras_sin_vocales(cadena):
    vocales = "aeiouAEIOU"
    return set([letra for letra in cadena if letra.lower() not in vocales])

cadena = "Esto no es una silumacion te rindes o luchas"
resultado = palabras_sin_vocales(cadena)
print(resultado) 