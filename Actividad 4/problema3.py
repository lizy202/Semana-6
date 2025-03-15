def contar_vocalesyconsonantes(palabra):
    vocales = "aeiouAEIOU"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count_vocales = 0
    count_consonantes = 0
    
    for letra in palabra:
        if letra in vocales:
            count_vocales += 1
        elif letra in consonantes:
            count_consonantes += 1
    
    return count_vocales, count_consonantes


palabra = "Esto no es una silumacion te rindes o luchas"
vocales, consonantes = contar_vocalesyconsonantes(palabra)
print("Vocales: ", vocales ," Consonantes: ", consonantes)