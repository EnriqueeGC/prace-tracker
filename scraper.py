import requests
from bs4  import BeautifulSoup

def getPrice(url):
    headers={'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # price container
        priceTag = soup.find(id='price-special')
        
        if priceTag:
            price = float(priceTag.text.strip().replace('Q', '').replace(',', ''))
            return price
        else:
            print('Error al encontrar el precio')
    else:
        print(f'Error al acceder a la pagina: {response.status_code}')