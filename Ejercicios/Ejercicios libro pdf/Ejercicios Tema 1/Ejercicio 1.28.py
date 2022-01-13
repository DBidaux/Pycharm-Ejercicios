temp_aire = float(input("Introduzca la temperatura en grados centígrados: "))
velo_viento = float(input("Introduzca la velocidad del viento en km/h: "))

if temp_aire >= 10:
    raise Exception("Tiene que ser una temperatura menor de 10ºC")
else:
    pass

if velo_viento < 4.8:
    raise Exception("Tiene que ser una velocidad superior a 4,8 km/h")
else:
    pass

wci = (13.12 + (0.6125 * temp_aire)) - (11.37 * (velo_viento**0.16)) + (0.3965 * (temp_aire * (velo_viento**0.16)))

print("El índice de Wind Chill es " + str(round(wci)))
