import bs4 as BeautifulSoup
import csv
import sys
import os
# sys.path.append(os.path.abspath(".."))
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)
import Investegra.backend.config.config_pags as config_pags

acesso = config_pags.Acesso()

def GetAcoes():
    
    if acesso.response_ações.status_code == 200:
        
        soup = BeautifulSoup.BeautifulSoup(acesso.response_ações.text, 'html.parser')
        table = soup.find('table', {'id': 'resultado'})
        
        if table:
            rows = table.find_all('tr')[1:] 
            data = []
            
            for row in rows:
                cols = row.find_all('td')
                cols = [col.text.strip() for col in cols]
                data.append(cols)
    
            with open(f'Investegra/env/ações/Dados_Acoes.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Código', 'Cotação', 'P/L', 'P/VP', 'RSR', 'DY', 'P/Ativo', 'P/Cap.Giro', 'P/EBIT', 'P/ACL', 'EV/EBITDA', 'EV/EBIT', 'Mrg.Liq', 'Lig.Corr', 'ROIC', 'ROE', 'Liquidez 2 meses', 'Patrimonio Líquido', 'Dív. Bruta/Patrimonio', 'Cresc. Rec. 5a'])
                writer.writerows(data)
                
            # with open('Investegra/env/ações/Dados_Acoes.csv', 'r', encoding='utf-8') as f:
            #     conteudo = f.read()

            # conteudo = conteudo.replace(',', ';')

            # with open('Investegra/env/ações/Dados_Acoes.csv', 'w', encoding='utf-8') as f:
            #     f.write(conteudo)
            
            print("Dados do Fundamentus salvos com sucesso!")
        else:
            print("Tabela de resultados não encontrada.")
    else:
        print(f"Erro: {acesso.response_ações.status_code}")
        
def GetFiis():
    
    if acesso.response_fiis.status_code == 200:
        
        
        soup = BeautifulSoup.BeautifulSoup(acesso.response_fiis.text, 'html.parser')
        table = soup.find('table', {'id': 'tabelaResultado'})
        
        if table:
            rows = table.find_all('tr')[1:]  
            data = []
            
            for row in rows:
                cols = row.find_all('td')
                cols = [col.text.strip() for col in cols]
                data.append(cols)
           
            
            with open(f'Investegra/env/fiis/Dados_Fiis.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Código', 'Empresa', 'Setor', 'Preço', 'P/VP', 'DY'])
                writer.writerows(data)
            
            print("Dados do Fundamentus salvos com sucesso!")
        else:
            print("Tabela de resultados não encontrada.")
    else:
        print(f"Erro: {acesso.response_fiis.status_code}")
        
def ReadCSV_Acoes():
    acoes = []
    with open(f'Investegra/env/ações/Dados_Acoes.csv', 'r', encoding='utf-8') as f:
        
        for linha in f.readlines()[1:]:
            Código,Cotação,P_L,P_VP,RSR,DY,P_Ativo,P_Cap_Giro,P_EBIT,P_ACL,EV_EBITDA,EV_EBIT,Mrg_Liq,Lig_Corr,ROIC,ROE,Liquidez_2_meses,Patrimonio_Líquido,Dív_Bruta_Patrimonio,Cresc_Rec_5a,_ = linha.strip().split(',')
            col = {
                'Código': Código,
                'Cotação': Cotação,
                'P/L': P_L,
                'P/VP': P_VP,
                'RSR': RSR,
                'DY': DY,
                'P/Ativo': P_Ativo,
                'P/Cap.Giro': P_Cap_Giro,
                'P/EBIT': P_EBIT,
                'P/ACL': P_ACL,
                'EV/EBITDA': EV_EBITDA,
                'EV/EBIT': EV_EBIT,
                'Mrg.Liq': Mrg_Liq,
                'Lig.Corr': Lig_Corr,
                'ROIC': ROIC,
                'ROE': ROE,
                'Liquidez 2 meses': Liquidez_2_meses,
                'Patrimonio Líquido': Patrimonio_Líquido,
                'Dív. Bruta/Patrimonio': Dív_Bruta_Patrimonio,
                'Cresc. Rec. 5a': Cresc_Rec_5a
            }
            acoes.append(col)
            
    return acoes

def ReadCSV_Fiis():
    with open(f'Investegra/env/fiis/Dados_Fiis.csv', 'r', encoding='utf-8') as f:
        for linha in f.readlines():
            print(linha.strip().split(','))
