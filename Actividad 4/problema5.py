def cifrado_cesar(cadena, desplazamiento):
    resultado = []
    for char in cadena:
        if char.isalpha():
            inicio = ord('a') if char.islower() else ord('A')
            resultado.append(chr((ord(char) - inicio + desplazamiento) % 26 + inicio))
        else:
            resultado.append(char)
    return ''.join(resultado)

texto = "Esto no es una silumacion te rindes o luchas"
desplazamiento = 3
print(cifrado_cesar(texto, desplazamiento)) 