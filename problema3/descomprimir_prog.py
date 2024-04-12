import zipfile

def descomprimir_zip(archivo_zip, directorio_destino):
    with zipfile.ZipFile(archivo_zip, 'r') as zip_ref:
        zip_ref.extractall(directorio_destino)

archivo_zip = 'perro_comprimido.zip'
directorio_destino = 'perro_descomprimido'
descomprimir_zip(archivo_zip= archivo_zip, directorio_destino= directorio_destino)

print(f"El archivo zip '{archivo_zip}' ha sido descomprimido en '{directorio_destino}'")