reservas = []

def validar_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Error, el campo no puede estar vacío.")
        def validar_entero_positivo(mensaje):
            while true:
                try:
                    numero = int(input(mensaje))
                    if numero >0:
                        return numero
                    else:
                        print("Error,debe ingresar un numero mayor a 0")
                except ValueError:
                    print("Error,debe ingresar un n umero valido")

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

#Funciones de calculo




        
