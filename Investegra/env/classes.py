import requests

class Acesso():
    url_ações = 'https://www.fundamentus.com.br/resultado.php'
    url_fiis = 'https://www.fundamentus.com.br/fii_resultado.php'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response_ações = requests.get(url_ações, headers=headers)
    response_fiis = requests.get(url_fiis, headers=headers)
    
class Usuario():
    nome = ""
    email = ""
    senha = ""
    
class Login():
    usuario = Usuario()
    
class Cadastro():
    usuario = Usuario()
    