from math import sqrt
diferencia_aceptable = 10**-12
x = float(input("Introduzca un número para calcular la raíz cuadrada: "))
prueba = x/2
resta = prueba**2 - x
real = sqrt(x)
if resta >= diferencia_aceptable:
    while resta != real:
        prueba_act = (prueba + (x/prueba)) / 2
        print(prueba_act)



