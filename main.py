from scraper import getPrice
from emailUtils import sendEmail
import json
import os

CONFIGFILE = 'config.json'

def loadConfig():
    with open(CONFIGFILE, 'r') as file:
        return json.load(file)
    
def main():
    config = loadConfig()
    url = config['url']
    targetPrice = config['target_price']

    currentPrice = getPrice(url)
    print(f'El precio actuala es: {currentPrice}')

    if currentPrice == targetPrice:
        subject = 'El precio coincide con tu objetivo'
        body = f'El precio del producto a alcanzado los {targetPrice}. COMPRA AHORA!'
        sendEmail(subject, body, config['email_to'])
        print('Correo de alerta enviado')
        
if __name__ == '__main__':
    main()