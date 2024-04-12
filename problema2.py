import random
from pyfiglet import Figlet

def seleccionar_fuente_aleatoria():
    fuentes = Figlet.getFonts()
    return random.choice(fuentes)

def main():
    figlet = Figlet()

    print("Lista de fuentes disponibles: ")
    print(figlet.getFonts())

    fuente_seleccionada = input("\nIngrese el nombre de la fuente a utilizar (obligatorio): ").strip()
    if fuente_seleccionada is None:
        fuente_seleccionada = seleccionar_fuente_aleatoria()

    texto_imprimir = input("Ingrese el texto a imprimir: ")

    figlet.setFont(font=fuente_seleccionada)
    texto_impreso = figlet.renderText(texto_imprimir)

    print("\nTexto impreso:")
    print(texto_impreso)

if __name__ == "__main__":
    main()