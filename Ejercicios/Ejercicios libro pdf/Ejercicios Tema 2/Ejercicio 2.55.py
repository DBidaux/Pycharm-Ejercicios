from math import pow

frecuencia = float(input("Introduzca una frecuencia en Hz: "))

if frecuencia > 3 * pow(10, 19):
    nombre = "Rayos gamma"
elif 3 * pow(10, 17) <= frecuencia < 3 * pow(10, 19):
    nombre = "Rayos X"
elif 7.5 * pow(10, 14) <= frecuencia < 3 * pow(10, 17):
    nombre = "Ultravioleta"
elif 4.3 * pow(10, 14) <= frecuencia < 7.5 * pow(10, 14):
    nombre = "Espectro visible"
elif 3 * pow(10, 12) <= frecuencia < 4.3 * pow(10, 14):
    nombre = "Infrarrojos"
elif 3 * pow(10, 9) <= frecuencia < 3 * pow(10, 12):
    nombre = "Microondas"
elif 3 * pow(10, 9) < frecuencia:
    nombre = "Onda de radio"
else:
    nombre = "No definido."

print("La longitud de onda con esa frecuencia se denomina:", nombre)
