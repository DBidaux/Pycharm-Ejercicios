# Escala de Richter (Comparativa son todas iguales!) Definir clases y comparar con if
magnitud = float(input("Introduzca una magnitud: "))
micro = 1.99
muypequeno = 2.99
pequeno = 3.99
suave = 4.99
moderado = 5.99
fuerte = 6.99
grande = 7.99
muygrande = 8.99
meteorico = 10

if magnitud < micro:
    print("El terremoto de esta magnitud es considerado un microsismo.")
elif magnitud < muypequeno:
    print("El terremoto de esta magnitud es considerado un sismo muy pequeño.")
elif magnitud < pequeno:
    print("El terremoto de esta magnitud es considerado un sismo pequeño.")
elif magnitud < suave:
    print("El terremoto de esta magnitud es considerado un sismo suave.")
elif magnitud < moderado:
    print("El terremoto de esta magnitud es considerado un sismo moderado.")
elif magnitud < fuerte:
    print("El terremoto de esta magnitud es considerado un sismo fuerte.")
elif magnitud < grande:
    print("El terremoto de esta magnitud es considerado un sismo grande.")
elif magnitud < muygrande:
    print("El terremoto de esta magnitud es considerado un sismo muy grande.")
elif magnitud < meteorico:
    print("El terremoto de esta magnitud es considerado un sismo meteórico.")
