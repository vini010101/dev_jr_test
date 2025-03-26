import requests

WEBHOOK_URL = "https://webhook.site/14578e8a-bdf0-49ae-9abf-6ed0c9169dab"  # Substitua com a URL do seu webhook

def send_city_to_webhook(city_data):
    """
    Envia os dados da cidade para o webhook.
    
    :param city_data: Dicionário com os dados da cidade.
    """
    try:
        # Envia os dados para o Webhook via POST
        response = requests.post(WEBHOOK_URL, json=city_data)
        
        if response.status_code == 200:
            print("Webhook enviado com sucesso!")
        else:
            print(f"Erro ao enviar o Webhook. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
