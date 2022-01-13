minimo = 20
maximo = 500
numero = int(input("Introduce un número: "))
if numero < minimo:
    print("Valor bajo")
elif minimo < numero < maximo:
    print("Valor medio")
else:
    print("Valor alto")