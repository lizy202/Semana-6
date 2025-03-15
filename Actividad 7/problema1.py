def diccionario_precios():
    precios = {
        "manzana": 1.2,
        "banana": 0.5,
        "naranja": 0.8,
        "pera": 1.0
    }

    producto = input("Ingrese el nombre del producto: ").lower()
    if producto in precios:
        print("El precio de ", producto," es: $", precios[producto])
    else:
        print("Producto no encontrado")

diccionario_precios()
