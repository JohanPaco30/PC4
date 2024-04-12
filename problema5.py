def GuardarTablaMultiplicar(numero):
    with open(f'tabla-{numero}.txt', 'w') as file:
        for i in range(1, 13):
            file.write(f'{numero} x {i} = {numero*i}\n')

def MostrarTablaMultiplicar(numero):
    try:
        with open(f'tabla-{numero}.txt', 'r') as file:
            print(f'\nLa tabla de multiplicar del numero {numero} es:\n')
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def MostrarLineaTablaMultiplicar(numero, linea):
    try:
        with open(f'tabla-{numero}.txt', 'r') as file:
            lines = file.readlines()
            if 1 <= linea <= 12:
                print(lines[linea-1])
            else:
                print("La línea especificada está fuera del rango válido.")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

# Menú para organizar el programa
opcion = 0
while opcion != 4:
    print("\nMenú:")
    print("1. Guardar tabla de multiplicar")
    print("2. Mostrar tabla de multiplicar")
    print("3. Mostrar línea de la tabla de multiplicar")
    print("4. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        numero = int(input("Ingrese un número entre 1 y 10: "))
        GuardarTablaMultiplicar(numero)
    elif opcion == 2:
        numero = int(input("Ingrese un número entre 1 y 10: "))
        MostrarTablaMultiplicar(numero)
    elif opcion == 3:
        numero = int(input("Ingrese un número entre 1 y 10: "))
        linea = int(input("Ingrese el número de línea a mostrar: "))
        MostrarLineaTablaMultiplicar(numero, linea)
    elif opcion == 4:
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Intente de nuevo.")

