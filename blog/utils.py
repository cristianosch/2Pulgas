import os
import requests
from core.settings import RAPIDAPI_KEY
import random

RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')



def get_random_quote_url():
    # Gerar um número aleatório entre 1 e 10 (ou o intervalo desejado)
    quote_number = random.randint(1, 50)  # Altere o intervalo conforme necessário
    
    # Construir a URL dinâmica com o número aleatório
    url = f"https://motivational-content.p.rapidapi.com/quotes/{quote_number}"
    
    return url


def get_quote():
    
    url = get_random_quote_url()  # Obter a URL dinâmica com número aleatório
    headers = {
        #"X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "motivational-content.p.rapidapi.com"
    }
    print(url)
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        quote_data = response.json()
        
        return quote_data["quote"]
    else:
        return "Unable to obtain quote at this time."
