import pandas as pd

# Especificar la URL del archivo CSV
csv_url = "https://github.com/gdelgador/Python-PC5/blob/main/src/airbnb.csv"

# Leer el archivo CSV
df_airbnb = pd.read_csv(csv_url)

# Condiciones del problema
condition = (df_airbnb['reviews'] > 10) & (df_airbnb['overall_satisfaction'] > 4)
condition_2 = (df_airbnb['accommodates'] == 4) & (df_airbnb['bedrooms'] == 3)

# Filtrar el DataFrame según las condiciones
df_filtered = df_airbnb[condition & condition_2]

# Ordenar por puntuación general y número de revisiones
df_ordered = df_filtered.sort_values(['overall_satisfaction', 'reviews'], ascending=[False, False])

# Obtener las 3 mejores opciones
top_3_options = df_ordered.head(3)

# Mostrar las 3 mejores opciones
print(top_3_options)
