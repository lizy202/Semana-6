import math

def ordenar_puntos(puntos):
    def distancia_origen(punto):
        x, y = punto
        return math.sqrt(x**2 + y**2)
    
    return sorted(puntos, key=distancia_origen)

puntos = [(1, 2), (3, 4), (0, 1), (5, 5)]
resultado = ordenar_puntos(puntos)
print("Puntos ordenados por distancia al origen:")
for punto in resultado:
    print(punto)
