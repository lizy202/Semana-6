def registro_temperaturas():
    temperaturas = []
    for dia in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]:
        temperatura = float(input(f"Ingrese la temperatura del {dia}: "))
        temperaturas.append((dia, temperatura))
    
    promedio = sum([temp for dia, temp in temperaturas]) / len(temperaturas)
    print("\nTemperatura promedio de la semana: ", promedio, "°C")

registro_temperaturas()
