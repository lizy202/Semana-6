def eliminar_elemento_conjunto(conjunto, elemento):
    if elemento in conjunto:
        conjunto.remove(elemento)
    return conjunto

conjunto = {1, 2, 3, 4}
elemento = 4
resultado = eliminar_elemento_conjunto(conjunto, elemento)
print(resultado) 