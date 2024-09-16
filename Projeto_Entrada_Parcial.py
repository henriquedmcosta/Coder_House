import pandas as pd
import requests
from plyer import notification

def notificacao():
    notification.notify(
        title = "Alerta",
        message = "Importação bem sucedida",
        app_name = "API",
        timeout = 10 )

def notificacao_1():
    notification.notify(
        title = "Alerta",
        message = "Importação mal sucedida",
        app_name = "API",
        timeout = 10 )

url = "https://brasilapi.com.br/api/banks/v1"
response = requests.get(url)
if response.status_code == 200:
    notificacao()
else:
    notificacao_1()  

    

