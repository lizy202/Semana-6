import math

def polar_a_cartesiana(coordenada_polar):
    r, theta = coordenada_polar
    x = r * math.cos(math.radians(theta))
    y = r * math.sin(math.radians(theta))
    return (x, y)

polar = (10, 15)
cartesiana = polar_a_cartesiana(polar)
print(cartesiana) 
