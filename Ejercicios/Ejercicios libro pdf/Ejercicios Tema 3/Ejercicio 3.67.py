precio_bebe = 0
precio_nino = 14.00
precio_adulto = 23.00
precio_abuelo = 18.00

limite_bebe = 2
limite_nino = 12
limite_adulto = 64

total = 0

linea = input("Introduzca la edad del cliente (en blanco para terminar): ")
while linea != "":
    edad = int(linea)
    if edad <= limite_bebe:
        total = total + precio_bebe
    elif edad <= limite_nino:
        total = total + precio_nino
    elif edad <= limite_adulto:
        total = total + precio_adulto
    else:
        total = total + precio_abuelo
    linea = input("Introduzca la edad del cliente (en blanco para terminar): ")

print("El total a pagar por el grupo es de €%.2f" % total)

