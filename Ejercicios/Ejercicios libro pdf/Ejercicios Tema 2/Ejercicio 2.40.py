a = float(input("Introduzca el lado A del triángulo: "))
b = float(input("Introduzca el lado B del triángulo: "))
c = float(input("Introduzca el lado C del triángulo: "))

if a == b == c:
    print("Es un triángulo equilátero.")
elif a == b or b == c or a == c:
    print("Es un triángulo isósceles.")
else:
    print("Es un triángulo escaleno.")
