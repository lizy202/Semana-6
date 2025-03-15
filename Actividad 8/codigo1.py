# Diccionario de películas con géneros y actores
peliculas = {
    'Inception': {
        'generos': ['acción', 'ciencia ficción', 'suspenso'],
        'actores': ['Leonardo DiCaprio', 'Joseph Gordon-Levitt', 'Ellen Page']
    },
    'The Matrix': {
        'generos': ['acción', 'ciencia ficción', 'thriller'],
        'actores': ['Keanu Reeves', 'Laurence Fishburne', 'Carrie-Anne Moss']
    },
    'The Lion King': {
        'generos': ['animación', 'aventura', 'drama'],
        'actores': ['Matthew Broderick', 'James Earl Jones', 'Jeremy Irons']
    },
    'Avengers: Endgame': {
        'generos': ['acción', 'aventura', 'ciencia ficción'],
        'actores': ['Robert Downey Jr.', 'Chris Evans', 'Scarlett Johansson']
    }
}

# Imprimir información de todas las películas
for pelicula, info in peliculas.items():
    print(f"Pelicula: {pelicula}")
    print(f"Géneros: {', '.join(info['generos'])}")
    print(f"Actores: {', '.join(info['actores'])}")
    print("-" * 40)
