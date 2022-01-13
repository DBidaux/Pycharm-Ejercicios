import random
import sys

numero = random.randint(0, 100)
MIN = 0
MAX = 100
minimo = MIN
maximo = MAX


def Pedir_Numero_Limite(minimo=MIN, maximo=MAX):
    while True:
        entrada = limites
        if minimo <= entrada <= maximo:
            return entrada


def Pedir_Numero(invitacion, minimo=MIN, maximo=MAX):
    invitacion = "Intente adivinar el numero entre " + str(minimo) + " y " + str(maximo) + ": "
    while True:
        entrada = input(invitacion)
        try:
            entrada = int(entrada)
        except:
            print("Solo estan autorizados los caracteres [0-9].",
                  file=sys.stderr)
        else:
            if minimo <= entrada <= maximo:
                break
    return entrada

limites = minimo, maximo
while True:
    minimo = Pedir_Numero_Limite(minimo)
    maximo = Pedir_Numero_Limite(maximo)
    if maximo > minimo:
        break
limites = Pedir_Numero_Limite("Introduzca limites inferior y superior", minimo, maximo)


while True:
    intento = Pedir_Numero("Adivine el número", minimo, maximo)
    if intento < numero:
        print("Demasiado pequeño")
        minimo = intento + 1
    elif intento > numero:
        print("Demasiado grande")
        maximo = intento - 1
    else:
        print("Ha ganado")
        break
