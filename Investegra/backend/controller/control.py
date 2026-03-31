import requests
from bs4 import BeautifulSoup


url = 'https://www.fundamentus.com.br/resultado.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
# 1. Pegar dados
response = requests.get(url, headers=headers)
html_content = response.text 

def RespostaPag():
    if response.status_code == 200:
        return "Página carregada com sucesso!"
    else:
        return f"Falha ao acessar. Código: {response.status_code}"

def ExtrairDados():
    
    if RespostaPag() == "Página carregada com sucesso!":

        soup = BeautifulSoup(html_content, 'html.parser')
        
        table = soup.find('table', {'id': 'resultado'})
        
    if table:
        rows = table.find_all('tr')[1:]  # Ignorar cabeçalho
        for row in rows:
            cols = row.find_all('td')
            data = [col.text.strip() for col in cols]
            print(data)  # Exibir dados extraídos
    else:
        print("Tabela não encontrada.")

RespostaPag()