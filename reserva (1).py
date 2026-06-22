reservas = []

def validar_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Error: el campo no puede estar vacío.")
