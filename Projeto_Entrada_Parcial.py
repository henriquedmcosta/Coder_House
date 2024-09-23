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
    
url_1 = "https://brasilapi.com.br/api/cep/v1/{cep}"
response_1 = requests.get(url_1)
if response_1.status_code == 200:
    notificacao()
else:
    notificacao_1()
    
url_2 = "https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
response_2 = requests.get(url_2)
if response_2.status_code == 200:
    notificacao()
else:
    notificacao_1()

df_bancos = pd.DataFrame(response.json())

df_cep = pd.DataFrame(response_1.json())

df_cnpj = pd.DataFrame(response_2.json())
