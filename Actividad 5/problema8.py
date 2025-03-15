import math

def distancia_euclidiana(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


punto1 = (1, 2)
punto2 = (9, 8)
distancia = distancia_euclidiana(punto1, punto2)
print(distancia)  
