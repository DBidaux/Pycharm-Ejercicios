# En el primer intento, me dió fallo porque en el bucle utilizaba siempre los mismos denominadores, por eso hay que
# meterlos en el bucle.
iteraciones = 15
primer = 2
segund = 3
tercer = 4
aprox_pos = + 4 / (primer * segund * tercer)
a = 4
b = 5
c = 6
aprox_neg = - 4 / (a * b * c)
base = 3
contador = 1
while iteraciones != 0:
    if contador % 2 != 0:
        base = base + (4 / (primer * segund * tercer))
        print("Aproximación", contador, ", el valor de pi es ", base)
        contador = contador + 1
        primer = primer + 4
        segund = segund + 4
        tercer = tercer + 4
        iteraciones = iteraciones - 1
    else:
        base = base + - (4 / (a * b * c))
        print("Aproximacion", contador, ", el valor de pi es ", base)
        contador = contador + 1
        a = a + 4
        b = b + 4
        c = c + 4
        iteraciones = iteraciones - 1
