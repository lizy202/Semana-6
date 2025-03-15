def obtener_iniciales(nombre_completo):
    nombres = nombre_completo.split()
    iniciales = ''.join([nombre[0].upper() for nombre in nombres])
    return iniciales

nombre="Lizbeth Salas Maldonado"
print(obtener_iniciales(nombre))