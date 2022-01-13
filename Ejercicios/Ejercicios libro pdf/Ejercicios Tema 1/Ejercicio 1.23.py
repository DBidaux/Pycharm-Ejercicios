from math import tan, pi
lado = float(input("Introduce la longitud en cm de los lados: "))
numero = float(input("Introduce el número de lados que tiene el polígono: "))
area = (numero * lado**2) / 4 * tan(pi / numero)
print("El área del polígono es de " + str(area) + " en cm2.")