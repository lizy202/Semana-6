def diferencia_conjuntos(conjunto1, conjunto2):
    return conjunto1.difference(conjunto2)


conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7}
resultado = diferencia_conjuntos(conjunto1, conjunto2)
print(resultado) 
