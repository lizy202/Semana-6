def registro_compras():
    total = 0
    while True:
        producto = input("Ingrese el nombre del producto o 'salir': ")
        if producto.lower() == "salir":
            break
        cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
        precio_unitario = float(input(f"Ingrese el precio unitario de {producto}: "))
        total += cantidad * precio_unitario
    
    print("\nEl total gastado es: $", total)

registro_compras()
