import requests

def precio_USD():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
        data = response.json()
        return data['bpi']['USD']['rate_float']
    except requests.RequestException as error:
        print(f"Error al conectarse a la API: {error}")
        return None
    
def precio_GBP():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
        data = response.json()
        return data['bpi']['GBP']['rate_float']
    except requests.RequestException as error:
        print(f"Error al conectarse a la API: {error}")
        return None
    
def precio_EUR():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
        data = response.json()
        return data['bpi']['EUR']['rate_float']
    except requests.RequestException as error:
        print(f"Error al conectarse a la API: {error}")
        return None

precio1_USD = precio_USD()
precio2_GBD = precio_GBP()
precio3_EUR = precio_EUR()

with open('precios_BITCOIN.txt', mode= 'w') as file:
    file.writelines([f'PRECIOS BITCOIN:\n',f'En USD es de: ${precio1_USD:,.4f}\n', f'En GBD es de: ${precio2_GBD:,.4f}\n', f'En EUR es de: ${precio3_EUR:,.4f}'])


