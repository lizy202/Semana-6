datosClima = {
    'lat': 28.5421,
    'lon': -81.379,
    'timezone': 'America/New_York',
    'timezone_offset': -18000,
    'daily': [
        {'dt': '09/Sep/24', 'temp': 26.33, 'pressure': 1020, 'humidity': 58},
        {'dt': '10/Sep/24', 'temp': 28.03, 'pressure': 1018, 'humidity': 47},
        {'dt': '11/Sep/24', 'temp': 28.93, 'pressure': 1018, 'humidity': 56},
        {'dt': '12/Sep/24', 'temp': 30.8, 'pressure': 1018, 'humidity': 46},
        {'dt': '13/Sep/24', 'temp': 27.17, 'pressure': 1019, 'humidity': 61},
        {'dt': '14/Sep/24', 'temp': 24.02, 'pressure': 1020, 'humidity': 67},
        {'dt': '17/Sep/24', 'temp': 23.73, 'pressure': 1023, 'humidity': 40},
        {'dt': '18/Sep/24', 'temp': 24.7, 'pressure': 1024, 'humidity': 39}
    ]
}

# 1. Obtener latitud y longitud
latitud = datosClima['lat']
longitud = datosClima['lon']
print("Latitud: ",latitud, "\nLongitud: ",longitud)

# 2. Imprimir el valor de la presión atmosférica el 11 de septiembre
presion_11_sep = None
for dia in datosClima['daily']:
    if dia['dt'] == '11/Sep/24':
        presion_11_sep = dia['pressure']
        break
print("La presión atmosférica el 11 de septiembre es: ",presion_11_sep, " hPa")

# 3. ¿Cuál es la humedad relativa el 13 de septiembre?
humedad_13_sep = None
for dia in datosClima['daily']:
    if dia['dt'] == '13/Sep/24':
        humedad_13_sep = dia['humidity']
        break
print("La humedad relativa el 13 de septiembre es: ",humedad_13_sep, "%")

# 4. Acceder a la lista completa de datos diarios
datos_diarios = datosClima['daily']
print("Datos completos de los días:")
for dia in datos_diarios:
    print(dia)

# 5. Obtener la temperatura registrada el 14 de septiembre
temperatura_14_sep = None
for dia in datosClima['daily']:
    if dia['dt'] == '14/Sep/24':
        temperatura_14_sep = dia['temp']
        break
print("La temperatura registrada el 14 de septiembre es: ", temperatura_14_sep, "°C")

# 6. Contar cuántos elementos hay en la lista 'daily'
cantidad_dias = len(datosClima['daily'])
print("Hay ", cantidad_dias, " elementos en la lista 'daily'.")
