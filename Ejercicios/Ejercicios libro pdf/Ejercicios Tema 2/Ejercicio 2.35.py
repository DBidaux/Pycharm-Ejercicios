primeros2a = 10.5
siguientesa = 4
anosperro = float(input("Introduzca los años del perrete: "))
primeros2anos = ((anosperro * primeros2a) - ((anosperro - 2) * primeros2a))
siguienteanos = primeros2anos + ((anosperro - 2) * siguientesa)

if 0 < anosperro < 2:
    print(primeros2anos)
elif anosperro <= 0:
    print("Introduce una edad correcta (número positivo).")
else:
    print(siguienteanos)
