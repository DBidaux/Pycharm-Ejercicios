import random

numero = random.randint(0, 100)
intento = -1
min = 0
max = 100

while intento != numero:
    last_input = intento
    intento = input("Adivine el numero del 0 al 100: ")
    try:
        intento = int(intento)
    except:
        continue
    if intento < 1 or intento > 100:
        continue

    if intento > numero:
        print("Demasiado pequeño! Prueba desde", intento + 1, "a", max)
        max = intento - 1

    elif intento < numero:
        print("Demasiado grande! Prueba desde", min, "a", intento - 1)
        min = intento + 1
print("Ha ganado!")
