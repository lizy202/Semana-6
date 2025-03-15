# Diccionario de países con información geográfica
paises = {
    'España': {
        'ciudades': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia'],
        'coordenadas': [
            {'latitud': 40.4168, 'longitud': -3.7038},  # Madrid
            {'latitud': 41.3784, 'longitud': 2.1926},   # Barcelona
            {'latitud': 37.3886, 'longitud': -5.9823},  # Sevilla
            {'latitud': 39.4699, 'longitud': -0.3763}   # Valencia
        ]
    },
    'Estados Unidos': {
        'ciudades': ['Nueva York', 'Los Ángeles', 'Chicago', 'Miami'],
        'coordenadas': [
            {'latitud': 40.7128, 'longitud': -74.0060},  # Nueva York
            {'latitud': 34.0522, 'longitud': -118.2437}, # Los Ángeles
            {'latitud': 41.8781, 'longitud': -87.6298},  # Chicago
            {'latitud': 25.7617, 'longitud': -80.1918}   # Miami
        ]
    },
    'México': {
        'ciudades': ['Ciudad de México', 'Guadalajara', 'Monterrey', 'Cancún'],
        'coordenadas': [
            {'latitud': 19.4326, 'longitud': -99.1332},  # Ciudad de México
            {'latitud': 20.6597, 'longitud': -103.3496}, # Guadalajara
            {'latitud': 25.6866, 'longitud': -100.3161}, # Monterrey
            {'latitud': 21.1743, 'longitud': -86.8466}   # Cancún
        ]
    }
}

# Imprimir información geográfica de todos los países
for pais, info in paises.items():
    print(f"País: {pais}")
    print(f"Ciudades importantes: {', '.join(info['ciudades'])}")
    for i, ciudad in enumerate(info['coordenadas']):
        print(f"Coordenadas de {info['ciudades'][i]}: Latitud: {ciudad['latitud']}, Longitud: {ciudad['longitud']}")
    print("-" * 40)
