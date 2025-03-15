def suma_diagonales(matriz):
    suma_diagonal_principal = 0
    suma_diagonal_secundaria = 0
    n = len(matriz)
    for i in range(n):
        suma_diagonal_principal += matriz[i][i]
        suma_diagonal_secundaria += matriz[i][n - 1 - i]
    return suma_diagonal_principal, suma_diagonal_secundaria


matriz = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],

]
diagonal_principal, diagonal_secundaria = suma_diagonales(matriz)
print("Suma diagonal principal: ", diagonal_principal, "Suma diagonal secundaria: ",diagonal_secundaria)
