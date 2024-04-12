import requests
import sqlite3

with sqlite3.connect('base.db') as conexion:
    c = conexion.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS sunat_info (fecha TEXT, compra_dolar REAL, venta_dolar REAL)''')

for mes in range(1, 13):
    año = 2023
    url = f'https://api.apis.net.pe/v1/tipo-cambio-sunat?month={mes}&year={año}'
    respuesta = requests.get(url)
    datos = respuesta.json()
    for item in datos:
        fecha = item['fecha']
        compra = item['compra']
        venta = item['venta']
        c.execute('INSERT INTO sunat_info VALUES (?, ?, ?)', (fecha, compra, venta))

conexion.commit()
conexion.close()
