def contar_lineas_codigo(ruta):
    if not ruta.endswith('.py'):
        print("El archivo no es un archivo Python (.py).")
        return

    try:
        with open(ruta, 'r') as file:
            lineas_codigo = 0
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    lineas_codigo += 1
            return lineas_codigo
    except FileNotFoundError:
        print("La ruta del archivo no es válida.")

ruta_archivo = input("Ingrese la ruta del archivo '.py': ")
cantidad_lineas = contar_lineas_codigo(ruta_archivo)

if cantidad_lineas is not None:
    print(f"El archivo '{ruta_archivo}' tiene {cantidad_lineas} líneas de código.")
