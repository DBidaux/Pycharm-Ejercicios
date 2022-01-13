import sys
from math import sqrt

# Raíces cuadradas y discriminantes
a = float(input("Introduce el término a:"))
b = float(input("Introduce el término b:"))
c = float(input("Introduce el término c:"))
bcuadrado = b ** 2
cuatroac = 4 * a * c
if cuatroac > bcuadrado:
    try:
        sqrt(bcuadrado - cuatroac)
    except ValueError as e:
        print("No se pueden hacer raíces negativas en este ejercicio.", file=sys.stderr)
        sys.exit()
discrim = sqrt(bcuadrado - cuatroac)
dosa = 2 * a

if discrim > 0:
    solucionp = -b + discrim / dosa
    solucionn = -b - discrim / dosa
    print("Tiene dos soluciones que son " + str(solucionp) + " y " + str(solucionn) + ".")
elif discrim == 0:
    solucion = -b / 2 * a
    print("Tiene una raíz real, que es " + str(solucion) + ".")
elif discrim < 0:
    print("No tiene ninguna raíz real.")
