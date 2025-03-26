import requests
from . import crud, models

WEBHOOK_URL = "https://webhook.site/14578e8a-bdf0-49ae-9abf-6ed0c9169dab"  # Substitua com a URL do seu webhook, estou utlizando essa URl personalizada

def send_data_to_webhook(data):
    """
    Envia os dados para o webhook.
    
    :param data: Dicionário com os dados da previsão.
    """
    try:
        # Envia os dados para o Webhook via POST
        response = requests.post(WEBHOOK_URL, json=data)
        
        if response.status_code == 200:
            print("Webhook enviado com sucesso!")
        else:
            print(f"Erro ao enviar o Webhook. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")

def verificar_e_enviar_para_webhook(db):
    """
    Verifica se existem novos dados no banco de dados e os envia para o webhook.
    """
    previsoes = crud.listar_previsoes(db)

    for previsao in previsoes:
        previsao_data = {
            "id": previsao.id,
            "cidade": previsao.cidade,
            "temperatura": previsao.temperatura,
            "data": previsao.data.isoformat(),  
        }
        send_data_to_webhook(previsao_data)
