def eliminar_duplicados(lista):
    return list(set(lista))

lista = [1, 2, 2, 2, 3, 4, 4, 5]
resultado = eliminar_duplicados(lista)
print(resultado) 