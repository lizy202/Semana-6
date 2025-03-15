def producto_escalar(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Los vectores deben tener la misma longitud")
    return sum(a * b for a, b in zip(v1, v2))


v1 = [1, 2, 3]
v2 = [7, 8, 9]
resultado = producto_escalar(v1, v2)
print(resultado) 
