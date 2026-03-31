import bs4
import requests

url = 'https://www.clubefii.com.br/fundo_imobiliario_lista'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)

def RespostaPag():
    if response.status_code == 200:
        print("Página carregada com sucesso!")
    else:
        print(f"Falha ao acessar. Código: {response.status_code}")

RespostaPag()