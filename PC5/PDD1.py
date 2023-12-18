import pandas as pd
import sqlite3

DB = 'candidates.db'
TABLE_NAME = 'candidate'


def almacenar_pandas_to_sql(df: pd.DataFrame, database_name: str, table_name: str) -> None:
    """Procesamiento datos candidatos para almacenarlos sobre db"""

    # Rename columns
    column_rename = {c: c.replace(' ', '') for c in df.columns}
    df.rename(column_rename, axis='columns', inplace=True)

    # Almaceno sobre db
    conn = sqlite3.connect(database_name)
    df.to_sql(table_name, conn, index=False, if_exists='replace')
    conn.close()

    cantidad_registros = df.shape[0]
    print(f'Se almacenaron {cantidad_registros} registros sobre tabla {table_name} en la base de datos {database_name}')


# Read csv
url = 'https://github.com/gdelgador/Python-PC5/raw/main/src/candidates.csv'
df = pd.read_csv(url, sep=';')

# Display shape and head
print(f'Shape del DataFrame: {df.shape}')
print('\nPrimeras 2 filas del DataFrame:')
print(df.head(2))

# Almacenar en base de datos SQLite
almacenar_pandas_to_sql(df, DB, TABLE_NAME)
