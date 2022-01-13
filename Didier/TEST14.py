import random
entrada = random.randint(0, 100)
MIN = 0
MAX = 100

def Pedir_Numero(invitacion, minimo, maximo):
    invitacion += "entre" + str(minimo) + " y" + str(maximo) + ": "
    while True:
        entrada = input(invitacion)
        try:
            entrada = int(entrada)
        except:
            pass
        else:
            if MIN <= entrada <= MAX:
                break
    return entrada

numero = Pedir_Numero()

while True:
    intento = Pedir_Numero()
    if intento < numero:
        print("Demasiado pequeño")
    elif intento > numero:
        print("Demasiado grande")
    else:
        print("Ha acertado")
        break