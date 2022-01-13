# Módulo math: funciones y constantes complejas.
# fabs: valor absoluto de un número.
# factorial: factorial de un número.
# gcd: máximo común divisor de dos números especificados.
# isnan: comprueba si es un número.
# log: logaritmo en base x. 2 parámetros: numero a calcular, y base del logaritmo.
# pow: calcula la potencia x. 2 parámetros, base y exponente.
# sqrt: calcula la raíz cuadrada.
# acos: arcocoseno en radianes.
# asin: arcoseno en radianes.
# atan: arcotangente en radianes.
# cos: coseno en radianes.
# sin: seno en radianes.
# tan: tangente en radianes.
# degrees: devuelve el valor en grados de un parámetro.
# radians: retorna el valor en radianes de un parámetro.
# pi: constante pi.
# e: constante e.
# tau: contante t.
# inf: representación de infinito.
# nan: NaN (Not a Number).

import math
print("----------Ejercicio 1:----------")
print("El valor absoluto de -7 es: ", math.fabs(-7))
print("El factorial de 9 es: ", math.factorial(9))
print("El máximo común divisor de 39 y 26 es: ", math.gcd(39,26))
print("isnan(8): ", math.isnan(8))
print("El logaritmo en base 10 de 540 es: ", math. log(540, 10))
print("El valor de 2 elevado a 10 es: ", math.pow(2, 10))
print("La raíz cuadrada de 144 es: ", math.sqrt(144))

print("----------Ejercicio 2:----------")
print("El ángulo 90 en radianes es: ", math.radians(90))
print("El ángulo 1.57 en grados es: ", math.degrees(1.57))
print("El seno de un ángulo de 180 es: ", math.sin(math.radians(180)))
print("El coseno de un ángulo de 180 es: ", math.cos(math.radians(180)))
print("La tangente de un ángulo de 180 es: ", math.tan(math.radians(180)))
print("El arcoseno de 1 es: ", math.degrees(math.asin(1)))
print("El arcocoseno de 1 es: ", math.degrees(math.acos(1)))
print("La arcotangente de 1 es: ", math.degrees(math.atan(1)))

print("----------Ejercicio 3:----------")
print("El valor de pi es: ", math.pi)
print("El valor de e es: ", math.e)
print("El valor de tau es: ", math.tau)
print("El valor de infinito es: ", math.inf)
print("El valor de NaN: ", math.nan)