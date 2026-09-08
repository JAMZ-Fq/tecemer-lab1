import requests
import json

URL = "https://api.open-meteo.com/v1/forecast"
PARAMETROS = {
    "latitude": -12.07, #Huancayo
    "longitude": -75.21,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "America/Lima",
    "forecast_days": 7,
}

"""try:
    respuesta = requests.get(URL,params=PARAMETROS,timeout=5)
    respuesta.raise_for_status()
    datos = respuesta.json()
except requests 
"""