import csv
import json
import requests

# --- Paso 2.2: Configuración de la API Open-Meteo para Huancayo ---
URL = "https://api.open-meteo.com/v1/forecast"
PARAMETROS = {
    "latitude": -12.07,  # Huancayo
    "longitude": -75.21,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "America/Lima",
    "forecast_days": 7,
}

try:
    respuesta = requests.get(URL, params=PARAMETROS, timeout=5)
    respuesta.raise_for_status()
    datos = respuesta.json()
except requests.exceptions.RequestException as error:
    raise SystemExit(f"No se pudo obtener el pronóstico: {error}")

# Mostrar estructura JSON del campo 'daily'
print("--- Respuesta JSON cruda ('daily') ---")
print(json.dumps(datos["daily"], indent=2, ensure_ascii=False))
print("-" * 40)

# --- Paso 2.3: Exploración de la estructura ---
print("Claves de primer nivel:", list(datos.keys()))
print('Claves de "daily":', list(datos["daily"].keys()))
print(
    'Tipo de "temperature_2m_max":', type(datos["daily"]["temperature_2m_max"])
)
print("Primer valor de tiempo:", datos["daily"]["time"][0])
print("-" * 40)

# --- Paso 2.4: Guardar JSON crudo y exportar a CSV ---
# 1. Guardar el JSON original para trazabilidad
with open("pronostico_huancayo.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, ensure_ascii=False, indent=2)

# 2. Construir y guardar el CSV
diario = datos["daily"]
filas = zip(
    diario["time"],
    diario["temperature_2m_max"],
    diario["temperature_2m_min"],
    diario["precipitation_sum"],
)

with open(
    "pronostico_huancayo.csv", "w", newline="", encoding="utf-8"
) as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["fecha", "temp_max", "temp_min", "precipitacion"])
    escritor.writerows(filas)

print(
    "¡Archivos 'pronostico_huancayo.json' y 'pronostico_huancayo.csv' generados con éxito!"
)