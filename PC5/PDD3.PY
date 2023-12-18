import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_password, receiver_email, subject, message, file_path):
    # Configuración del servidor SMTP de Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Crear instancia de MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Agregar cuerpo del mensaje
    msg.attach(MIMEText(message, 'plain'))

    # Adjuntar archivo
    attachment = open(file_path, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % file_path)
    msg.attach(part)

    # Conectar al servidor SMTP y enviar correo
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)

# Configuración de ejemplo
sender_email = 'tu_email@gmail.com'
sender_password = 'tu_contraseña'
receiver_email = 'destinatario@gmail.com'
subject = 'Reporte Brazil'
message = 'Reporte excel Brazil'
archivo_adjunto = 'Brazil.xlsx'  # Ajusta el nombre del archivo

# Llamada a la función de envío de correo
send_email(sender_email, sender_password, receiver_email, subject, message, archivo_adjunto)
