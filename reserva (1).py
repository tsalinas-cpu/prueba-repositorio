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
    


def registrar_reserva():
    print("\n====Registrar Reserva====")

    codigo = validar_texto("Ingrese el código de la reserva: ")

    if buscar_posicion(codigo) != -1:
        print("Error, el código ya existe.")
        return
    
    nombre = validar_texto("Nombre huesped: ")
    noches = validar_entero_positivo("Noches: ")
    valor_noche = validar_float_positivo("Valor noche: ")
    
    total = calcular_total(noches, valor_noche)
    categoria = calcular_categoria(total)

    reserva = {
        "codigo": codigo,
        "nombre": nombre,
        "noches": noches,
        "valor_noche": valor_noche,
        "total": total,
        "categoria": categoria
    }
    reservas.append(reserva)
    print("reserva registrada exitosamente.")

def buscar_reserva():
    print("\n====BUSCAR RESERVA====")
    codigo = validar_texto("Ingrese codigo:")
    posicion = buscar_posicicon(codigo)

if posicion == -1:
    print("Reserva no encontrada")
else:
    reserva = reseervas [posicion]

print(f"\nposicion: {posicion}")
print(f"Codigo: {reserva["codigo"]}")
print(f"Nombre: {reserva["nombre"]}")
print(f"Noches: {reserva["noches"]}")
print(f"Valor noche:${reserva["valor noche]:,.0f}")
print(f"total: ${reserva["total"]:,.0f}")
print(f"Categoria: {reserva["categoria"]}")


def actualizar_reserva():
print("\n====ACTUALIZAR RESERVA====")
codigo = validar_texto("Ingrese codigo:")
posicion = buscar_posicion(codigo)

if posicion == -1:
print("Reserva no encontrada")
return

reserva = reservas [posicion]
print("Ingrese los datos nuevos:")

reseerva["nombre"] = validar_texto("nombre:")
reserva["noches"] = validar_entero_positivo("Cantidad de noches:")
reserva["valor_noche"] = validar_float_positivo("Valor por noche:")

reserva["total"] = calcular_total(
reserva["noches"],
reserva[valor_noche])

reserva ["categoria"] = calcular_categoria(
reserva["total"])

print("Reserva actualizada correctamente")

def eliminar_reserva():
print("\n====ELIMINIR RESERVA====")

codigo = validar_texto("ingrese codigo:")

posicion = buscar_posicion(codigo)
if posicion == -1:
print("Reserva no encontrada")
else:
reservas.pop(posicion)
print("Reserva eliminada correctamente")






