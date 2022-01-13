from math import pi

radio = float(input("Introduzca el radio en cm: "))
area_circulo = pi * radio ** 2
volumen_esfera = ((4 / 3) * pi * radio ** 3)

print("El área del círculo es: " + str(area_circulo) + "cm2")
print("El volumen de la esfera es: " + str(volumen_esfera) + "cm3")
