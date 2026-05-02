sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
import sys
import os

from Investegra.env.classes import *

def CarregarPagAcoes():
    acesso = Acesso()
    if acesso.response_ações.status_code == 200:
        return "Página carregada com sucesso!"
    else:
        print(f"Falha ao acessar. Código: {acesso.response_ações.status_code}")

def CarregarPagFiis():
    acesso = Acesso()
    if acesso.response_fiis.status_code == 200:
        return "Página carregada com sucesso!"
    else: 
        print(f"Falha ao acessar. Código: {acesso.response_fiis.status_code}")

def CarregarPagCripto(url):
    acesso = Acesso()
    if url == 200:
        return "Página carregada com sucesso!"
    else: 
        print(f"Falha ao acessar. Código: {url.status_code}")

def CarregarPagEtfs():
    acesso = Acesso()
    if acesso.response_etfs.status_code == 200:
        return "Página carregada com sucesso!"
    else: 
        print(f"Falha ao acessar. Código: {acesso.response_etfs.status_code}")

def CarregarPagBdrs():
    acesso = Acesso()
    if acesso.response_bdrs.status_code == 200:
        return "Página carregada com sucesso!"
    else: 
        print(f"Falha ao acessar. Código: {acesso.response_bdrs.status_code}")