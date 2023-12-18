import pandas as pd

# Especificar la URL del archivo CSV
csv_url = "https://github.com/gdelgador/Python-PC5/blob/main/src/airbnb.csv"

# Leer el archivo CSV
df_airbnb = pd.read_csv(csv_url)

# IDs de las casas de Roberto y Clara
id_roberto = 97503
id_clara = 90387

# Filtrar propiedades de Roberto y Clara
roberto_property = df_airbnb[df_airbnb['room_id'] == id_roberto]
clara_property = df_airbnb[df_airbnb['room_id'] == id_clara]

# Verificar si las ID existen en el DataFrame
if roberto_property.empty or clara_property.empty:
    print("Una o ambas ID no existen en el DataFrame.")
else:
    # Comparar el número de críticas
    if roberto_property['reviews'].values[0] > clara_property['reviews'].values[0]:
        print("La casa de Roberto tiene más críticas que la de Clara.")
    elif roberto_property['reviews'].values[0] < clara_property['reviews'].values[0]:
        print("La casa de Clara tiene más críticas que la de Roberto.")
    else:
        print("Ambas casas tienen el mismo número de críticas.")

    # Crear un DataFrame con las propiedades de Roberto y Clara
    df_roberto_clara = pd.concat([roberto_property, clara_property])

    # Guardar el DataFrame como un archivo Excel
    df_roberto_clara.to_excel("roberto.xls", index=False)
