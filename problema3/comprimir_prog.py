import zipfile

nombre_archivo_zip = 'perro_comprimido.zip'
nombre_imagen = 'perro.jpg'

with zipfile.ZipFile(nombre_archivo_zip, 'w') as zipf:
    zipf.write(nombre_imagen)

print(f"La imagen ha sido comprimida como '{nombre_archivo_zip}'")
