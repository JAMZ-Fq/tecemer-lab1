import pandas as pd

# 1. Carga y preparación del dataset
df = pd.read_csv("pronostico_huancayo.csv")
df["fecha"] = pd.to_datetime(df["fecha"])

print("--- Primeros registros ---")
print(df.head())
print("\n--- Información del DataFrame ---")
print(df.info())
print("-" * 50)

# 2. Transformaciones y nuevas columnas
df["amplitud_termica"] = df["temp_max"] - df["temp_min"]
df["dia_lluvioso"] = df["precipitacion"] > 0
df["categoria"] = df["temp_max"].apply(
    lambda t: "cálido" if t >= 20 else ("templado" if t >= 15 else "frío")
)

print("\n--- DataFrame Transformado ---")
print(df)
print("\n--- Estadística Descriptiva ---")
print(df.describe())
print("-" * 50)

# 3. Agregaciones
resumen = df.groupby("categoria").agg(
    dias=("categoria", "count"),
    temp_max_promedio=("temp_max", "mean"),
    precipitacion_total=("precipitacion", "sum"),
)

print("\n--- Resumen por Categoría ---")
print(resumen)
print("-" * 50)

# 4. Exportación de resultados
df.to_csv("pronostico_huancayo_procesado.csv", index=False)
resumen.to_csv("resumen_por_categoria.csv")
print(
    "\n¡Archivos 'pronostico_huancayo_procesado.csv' y 'resumen_por_categoria.csv' exportados con éxito!"
)