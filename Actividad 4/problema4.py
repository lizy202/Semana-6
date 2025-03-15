def eliminar_espacios(cadena):
    return ' '.join(cadena.split())

cadena ="       Esto no    es una silumacion te    rindes o    luchas"
print(eliminar_espacios(cadena))