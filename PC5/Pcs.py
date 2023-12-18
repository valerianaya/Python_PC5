import pandas as pd
import sqlite3
import os

# Especificar la URL del archivo CSV
csv_url = "https://github.com/gdelgador/Python-PC5/blob/main/src/airbnb.csv"

# Leer el archivo CSV
df_airbnb = pd.read_csv(csv_url)


# Cargar los datos en un DataFrame
df_crypto = pd.read_excel('https://github.com/gdelgador/Python-PC5/raw/main/src/crypto_currency.xlsx')

# Crear o conectar a la base de datos SQLite
conn = sqlite3.connect('crypto_data.db')

# Guardar el DataFrame en una tabla de la base de datos
df_crypto.to_sql('crypto_data', conn, index=False, if_exists='replace')

# Cerrar la conexión
conn.close()


# Conectar a la base de datos SQLite
conn = sqlite3.connect('crypto_data.db')

# Leer los datos en un DataFrame
df_crypto_db = pd.read_sql_query('SELECT * FROM crypto_data', conn)

# Cerrar la conexión
conn.close()


# Crear una nueva columna 'TipoMoneda' con el tipo de moneda
df_crypto_db['TipoMoneda'] = 'Cripto'

# Crear un DataFrame con la información concatenada
df_concatenado = pd.concat([df_crypto_db, df_airbnb], ignore_index=True)


# Agrupar por tipo de moneda y obtener un resumen
resumen = df_concatenado.groupby('TipoMoneda').agg({
    'Precio': ['mean', 'min', 'max'],
    'Volumen': 'sum'
}).reset_index()


# Guardar el resumen en un archivo Excel
resumen.to_excel('resumen_crypto_airbnb.xlsx', index=False)


import matplotlib.pyplot as plt

# Crear un gráfico de barras del resumen
resumen.plot(x='TipoMoneda', y=('Precio', 'mean'), kind='bar', legend=False)
plt.xlabel('Tipo de Moneda')
plt.ylabel('Precio Promedio')
plt.title('Precio Promedio por Tipo de Moneda')
plt.savefig('grafico_resumen.png', dpi=300, bbox_inches='tight')
plt.close()


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_password, receiver_email, subject, message, archivo_adjunto=None, imagen_adjunta=None):
    # Configuración del servidor SMTP (en este caso, para Gmail)
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Crear un objeto SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)

    # Iniciar conexión TLS
    server.starttls()

    # Iniciar sesión en la cuenta de correo electrónico
    server.login(sender_email, sender_password)

    # Crear el mensaje de correo electrónico
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Agregar el cuerpo del mensaje
    msg.attach(MIMEText(message, 'plain'))

    # Adjuntar archivo si se proporciona
    if archivo_adjunto:
        attachment = open(archivo_adjunto, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={archivo_adjunto}')
        msg.attach(part)

    # Adjuntar imagen si se proporciona
    if imagen_adjunta:
        img_data = open(imagen_adjunta, 'rb').read()
        image = MIMEImage(img_data, name=os.path.basename(imagen_adjunta))
        msg.attach(image)

    # Enviar el mensaje de correo electrónico
    server.sendmail(sender_email, receiver_email, msg.as_string())

    # Cerrar la conexión
    server.quit()

# Uso de la función send_email
send_email(sender_email='valeanaya2003@gmail.com',
           sender_password='123581121',
           receiver_email='shgri@gmail.com',
           subject='Asunto del Correo',
           message='Cuerpo del Correo',
           archivo_adjunto='archivo_adjunto.txt',
           imagen_adjunta='imagen_adjunta.png')

