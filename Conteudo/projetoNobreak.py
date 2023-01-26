import os
from platform import system
import subprocess
import smtplib
import email.message

def check_ping(hostname, silent=True):
    argNPackages = "-n" if system().lower() == "windows" else "-c"
    command = ["ping", hostname, argNPackages, "1"]
    response = (
        subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        if silent
        else subprocess.call(command)
    )
    return response == 0

def enviar_email():
    corpo_email = """
    <p>Possivel ativação do Nobreak. Desligue os Servidores!</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "NOBREAK ATIVADO"
    msg['From'] = '' # email de quem vai enviar
    msg['To'] = ''   # email de quem vai receber a informação
    password = ''    # senha do email
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

def desligandoServidor():
    shutdown = os.system('shutdown -s')

resultado = check_ping('') # ip que vai ser pingado
if resultado == True:
    print("Equipamento ativo")
else:
    enviar_email()
    desligandoServidor()