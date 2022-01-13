c4 = 261.63
d4 = 293.66
e4 = 329.63
f4 = 349.23
g4 = 392.00
a4 = 440.00
b4 = 493.88

nombre = input("Introduzca una nota, en su notación de dos caracteres: ")
nota = nombre[0]
octava = int(nombre[1])

if nota == "c":
    frec = c4
elif nota == "d":
    frec = d4
elif nota == "e":
    frec = e4
elif nota == "f":
    frec = f4
elif nota == "g":
    frec = g4
elif nota == "a":
    frec = a4
elif nota == "b":
    frec = b4

frecfin = frec / 2 ** (4 - octava)

print("La frecuencia de", nombre, "es", frecfin)
