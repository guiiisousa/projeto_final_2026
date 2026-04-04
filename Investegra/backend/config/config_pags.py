import sys
import os
sys.path.append(os.path.abspath(".."))
import sys
print(sys.path)
from Investegra.env.classes import *


#Recarregar o fundamentus#
def RecarregarPagFundamentus_Acoes():
    acesso = Acesso()
    if acesso.response_ações.status_code == 200:
        print("Página carregada com sucesso!")
    else:
        print(f"Falha ao acessar. Código: {acesso.response_ações.status_code}")

def RecarregarPagFundamentus_Fiis():
    acesso = Acesso()
    if acesso.response_fiis.status_code == 200:
        print("Página carregada com sucesso!")
    else:
        print(f"Falha ao acessar. Código: {acesso.response_fiis.status_code}")

RecarregarPagFundamentus_Acoes()
RecarregarPagFundamentus_Fiis()
