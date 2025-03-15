def reversa_palabras(frase):
    palabras = frase.split()  
    palabras_volteadas = [palabra[::-1] for palabra in palabras]  
    return ' '.join(palabras_volteadas)

frase = "NO ES UN SIMULACRO"
print(reversa_palabras(frase)) 
