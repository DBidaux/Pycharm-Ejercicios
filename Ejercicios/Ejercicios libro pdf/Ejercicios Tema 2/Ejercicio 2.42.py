frecuencia = float(input("Introduzca una frecuencia, en Hz: "))

c4 = 261.63
d4 = 293.66
e4 = 329.63
f4 = 349.23
g4 = 392.00
a4 = 440.00
b4 = 493.88

if frecuencia == c4:
    print("La nota correspondiente a esta frecuencia es C4")
elif frecuencia == d4:
    print("La nota correspondiente a esta frecuencia es D4")
elif frecuencia == e4:
    print("La nota correspondiente a esta frecuencia es E4")
elif frecuencia == f4:
    print("La nota correspondiente a esta frecuencia es F4")
elif frecuencia == g4:
    print("La nota correspondiente a esta frecuencia es G4")
elif frecuencia == a4:
    print("La nota correspondiente a esta frecuencia es A4")
elif frecuencia == b4:
    print("La nota correspondiente a esta frecuencia es B4")
else:
    print("Esa frecuencia no corresponde a ninguna nota conocida.")
