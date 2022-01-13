mi_numero = 19
intento = 0
max_intento = 3
while intento < max_intento:
    pruebanumero = int(input("Adivina el número: "))
    intento += 1
    if pruebanumero == mi_numero:
        print("Eres un máquina!!")
        break
    else:
        print("Sigue intentándolo!")
else:
    print("Se te acabaron las oportunidades.")