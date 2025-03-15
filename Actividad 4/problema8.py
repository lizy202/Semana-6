def ordenar_longitud(palabras):
    return sorted(palabras, key=len)

palabras =["rojo", "azul", "naranja", "amarillo", "verde", "purpura"]
print(ordenar_longitud(palabras))
