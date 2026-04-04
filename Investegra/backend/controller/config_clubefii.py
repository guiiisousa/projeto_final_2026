# import bs4 as BeautifulSoup
# import csv
# import cloudscraper

# def GetDadosClubefii():
#     url = 'https://www.clubefii.com.br/fundo_imobiliario_lista'
    
#     scraper = cloudscraper.create_scraper()
#     response = scraper.get(url)

#     if response.status_code == 200:
#         print("Página carregada com sucesso!")
#         soup = BeautifulSoup.BeautifulSoup(response.text, 'html.parser')
#         table = soup.find('table', {'id': 'fii-table'})
        
#         if table:
#             rows = table.find_all('tr')[1:]  # Ignorar o cabeçalho
#             data = []
            
#             for row in rows:
#                 cols = row.find_all('td')
#                 cols = [col.text.strip() for col in cols]
#                 data.append(cols)
            
#             # Salvar os dados em um arquivo CSV
#             with open('clubefii_data.csv', 'w', newline='', encoding='utf-8') as f:
#                 writer = csv.writer(f)
#                 writer.writerow(['Código', 'Nome', 'Setor', 'Preço', 'P/VP', 'DY', 'Variação'])
#                 writer.writerows(data)
            
#             print("Dados do Clubefii salvos com sucesso!")
#         else:
#             print("Tabela de resultados não encontrada.")
#     else:
#         print(f"Erro: {response.status_code}")
        