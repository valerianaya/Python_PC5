import pandas as pd

# Especificar la URL del archivo CSV
csv_url = "https://github.com/gdelgador/Python-PC5/blob/main/src/airbnb.csv"

# Leer el archivo CSV
df_airbnb = pd.read_csv(csv_url)

# Condiciones para Diana
condition_diana = (df_airbnb['accommodates'] == 1) & (df_airbnb['price'] <= 50)

# Filtrar propiedades para Diana
df_diana = df_airbnb[condition_diana]

# Ordenar por precio ascendente y puntuación descendente para habitaciones compartidas
df_diana_shared = df_diana[df_diana['room_type'] == 'Shared room']
df_diana_shared = df_diana_shared.sort_values(['price', 'overall_satisfaction'], ascending=[True, False])

# Seleccionar las 10 propiedades más baratas
top_10_properties = df_diana_shared.head(10)

# Mostrar el resultado
print(top_10_properties[['room_id', 'neighborhood', 'price', 'overall_satisfaction']])
