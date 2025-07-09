import os
import requests
from django.conf import settings
import random
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
RAPIDAPI_KEY = str(os.getenv('RAPIDAPI_KEY'))



def get_random_quote_url():
    '''                   # ELIMINAR DO COMMENT EM PRODUÇÃO

    # Gerar um número aleatório entre 1 e 10 (ou o intervalo desejado)
    quote_number = random.randint(1, 50)  # Altere o intervalo conforme necessário
    
    # Construir a URL dinâmica com o número aleatório
    url = f"https://motivational-content.p.rapidapi.com/quotes/{quote_number}"
    
    return url
    '''
    pass


def get_quote():

    '''                 # ELIMINAR DO COMMENT EM PRODUÇÃO
    
    url = get_random_quote_url()  # Obter a URL dinâmica com número aleatório
    headers = {
        #"X-RapidAPI-Key": RAPIDAPI_KEY,
        #"X-RapidAPI-Host": "motivational-content.p.rapidapi.com"
    }
    print(url)
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        quote_data = response.json()
        
        return quote_data["quote"]
    else:
        return "Unable to obtain quote at this time."

    '''
    pass