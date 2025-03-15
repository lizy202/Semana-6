def suma_matrices(matriz1, matriz2):
    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[i])):
            fila.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(fila)
    return resultado


matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz2 = [[19, 18, 17], [16, 15, 14], [13, 12, 11]]
resultado = suma_matrices(matriz1, matriz2)
for fila in resultado:
    print(fila)
