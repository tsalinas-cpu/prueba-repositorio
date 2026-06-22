reservas = []

def validar_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Error, el campo no puede estar vacío.")

def validar_entero_positivo(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            else:
                print("Error, el número debe ser mayor a 0.")
        except ValueError:
            print("Error, debe ingresar un valor válido.")


def validar_float_positivo (mensaje):
    while true:
        try:
            numero = float(input(mensaje))
            if numero >0:
                return numero
            else:
                print("Error,numero debe ser mayor a 0")
        except ValueError:
            print("Error,debe ingresar un valor valido")

def calcular_total(noches,valor_noche):
    return noches * valor_noche

def calcular_categoria(total):
    if total < 200000:
        return "Económica"
    elif total < 500000:
        return "Estándar"
    else:
        return "premium"

def buscar_posicion(codigo):
    for i in range(len(reservas)):
        if reservas[i][0] == codigo:
            return i
        return -1
    




        
