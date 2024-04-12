import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()  # Verificar si hubo algún error en la solicitud
        data = response.json()
        return data['bpi']['USD']['rate_float']
    except requests.RequestException as error:
        print(f"Error al conectarse a la API: {error}")
        return None

def main():
    n = float(input("Ingrese la cantidad de bitcoins que posee: "))
    precio_bitcoin = obtener_precio_bitcoin()

    if precio_bitcoin is not None:
        costo_actual_usd = n * precio_bitcoin
        print(f"El costo actual de {n} Bitcoins en USD es: ${costo_actual_usd:,.4f}")

if __name__ == "__main__":
    main()