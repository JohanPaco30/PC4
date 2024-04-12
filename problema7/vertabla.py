import sqlite3
from pprint import pprint

with sqlite3.connect('base.db') as conexion:
    c = conexion.cursor()

    c.execute('SELECT * FROM sunat_info')
    filas = c.fetchall()


for fila in filas:
    pprint(fila)

conexion.close()