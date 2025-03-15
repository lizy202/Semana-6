def matriz_transpuesta(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
resultado = matriz_transpuesta(matriz)
for fila in resultado:
    print(fila)
