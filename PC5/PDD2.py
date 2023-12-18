import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB = 'candidates.db'
TABLE_NAME = 'candidate'

# 1. Lectura de datos
with sqlite3.connect(DB) as conn:
    df = pd.read_sql_query(f'select * from {TABLE_NAME}', conn)

# 2. Filtrado de datos
listado_paises = ['United States of America', 'Brazil', 'Colombia', 'Ecuador']
filterDf = df[(df['Country'].isin(listado_paises)) & (df['CodeChallengeScore'] >= 7) & (df['TechnicalInterviewScore'] >= 7)]

# 3. Crear y almacenar gráficos
def genero_grafico_circular(df: pd.DataFrame, country: str) -> None:
    tec = df.groupby('Technology')['Technology'].count()
    tec.plot.pie(figsize=(11, 7))
    plt.savefig(f"./reportes/images/{country}/pie_chart.png", dpi=300, bbox_inches='tight')
    plt.close()
    print(f'Se generó gráfico circular para {country}...')

def genero_grafico_barras(df: pd.DataFrame, country: str) -> None:
    senority_group = df.groupby('Seniority')['Seniority'].count()
    senority_group.plot.bar()
    plt.savefig(f"./reportes/images/{country}/bar_chart.png", dpi=300, bbox_inches='tight')
    plt.close()
    print(f'Se generó gráfico de barras para {country}...')

# 4. Generar carpetas necesarias
if not os.path.isdir('./reportes'):
    os.mkdir('reportes')
    os.mkdir('./reportes/images')

# 5. Iterar sobre los países
for country in listado_paises:
    # Crear subcarpetas
    if not os.path.isdir(f'./reportes/images/{country}'):
        os.mkdir(f'./reportes/images/{country}')

    # Filtrar df
    countryDf = filterDf[filterDf['Country'] == country]

    # Generar gráficos
    genero_grafico_circular(countryDf, country)
    genero_grafico_barras(countryDf, country)

    # Generar reporte Excel por país
    with pd.ExcelWriter(f"./reportes/{country}.xlsx", engine="xlsxwriter") as excelBook:
        sheet_name = f"Report-{country}"
        countryDf.to_excel(excelBook, index=False, sheet_name=sheet_name)

        # Posicionar sobre la hoja de Excel
        excel_sheet = excelBook.sheets[sheet_name]

        # Almacenar imágenes
        image_pie_path = f"./reportes/images/{country}/pie_chart.png"
        image_bar_path = f"./reportes/images/{country}/bar_chart.png"

        excel_sheet.insert_image(1, countryDf.shape[1] + 2, image_pie_path)
        excel_sheet.insert_image(countryDf.shape[0] + 2, countryDf.shape[1] + 2, image_bar_path)

        print(f'Se generó un informe para el país {country}')

print('Se finalizó la generación de informes.')
