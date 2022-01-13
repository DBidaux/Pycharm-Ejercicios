from math import pi

radio_cilindro = float(input("Introduce el radio de la base del cilindro: "))
altura_cilindro = float(input("Introduzca la altura del cilindro: "))
area_cilindro = pi * (radio_cilindro ** 2)
volumen_cilindro = area_cilindro * altura_cilindro
print("El volumen del cilindro es %.1f cm3." % volumen_cilindro)
