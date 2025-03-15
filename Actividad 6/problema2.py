def es_subconjunto(conjunto1, conjunto2):
    return conjunto1.issubset(conjunto2)

conjunto1 = {1, 2}
conjunto2 = {1, 2, 3, 4}
resultado = es_subconjunto(conjunto1, conjunto2)
print(resultado) 