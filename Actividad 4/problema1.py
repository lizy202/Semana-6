def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

texto = "Esto no es una silumacion te rindes o luchas"
print(contar_palabras(texto))