import smtplib
from email.mime.text import MIMEText

'''
# Configurações outlook
smtp_server = 'smtp.office365.com'
smtp_port = 587
email = 'cristiano.dev@outlook.com'
password = '@Goodvibes123'
'''


# Configurações gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
email = '2pulgass@gmail.com'
password = '@2Pulgas123'

# Mensagem
msg = MIMEText('Corpo do email.')
msg['Subject'] = 'Assunto do Email'
msg['From'] = email
msg['To'] = 'destinatario@example.com'

# Envio do email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, [msg['To']], msg.as_string())
    server.quit()
    print("Email enviado com sucesso!")
except smtplib.SMTPAuthenticationError as e:
    print(f"Erro de autenticação: {e}")
except Exception as e:
    print(f"SMTP authentication error: {e}")





