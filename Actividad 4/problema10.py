def eliminar_impares(lista):
    return [x for x in lista if x % 2 == 0]

lista = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 15, 21, 22, 23, 24, 25]
print(eliminar_impares(lista)) 