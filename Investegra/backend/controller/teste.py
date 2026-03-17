from brapi import Brapi
# from flask import Flask, render_template
import requests


# client = Brapi(api_key='YOUR_TOKEN')
# quotes = client.quote.retrieve(
#     tickers='PETR4',
#     range='5d',
#     interval='1d',
#     fundamental=True
# )

# print(quotes.results[0].regular_market_price)

url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=demo'
r = requests.get(url)
data = r.json()

print(data)