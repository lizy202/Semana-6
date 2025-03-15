def buscar_elemento(matriz, elemento):
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == elemento:
                return (i, j) 
    return None  

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
elemento = 9
resultado = buscar_elemento(matriz, elemento)
print(resultado)  
