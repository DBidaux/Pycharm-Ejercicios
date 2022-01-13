from random import randrange

valor = randrange(0, 38)
if valor == 37:
    print("El resultado es 00")
else:
    print("El resultado es %d" % valor)

if valor == 37:
    print("Se paga a 00")
else:
    print("Se paga a", valor)

if valor % 2 == 1 and 1 <= valor <= 9 or \
        valor % 2 == 0 and 12 <= valor <= 18 or \
        valor % 2 == 0 and 19 <= valor <= 27 or \
        valor % 2 == 0 and 30 <= valor <= 36:
    print("Se paga al rojo")
elif valor == 0 or valor == 37:
    pass
else:
    print("Se paga al negro")

if 1 <= valor <= 36:
    if valor % 2 == 1:
        print("Se paga a impar")
    else:
        print("Se paga a par")

if 1 <= valor <= 18:
    print("Se paga de 1 a 18")
elif 19 <= valor <= 36:
    print("Se paga de 19 a 36")
