wavelenght = float(input("Introduzca una longitud de onda para saber el color: "))

if 370 > wavelenght:
    print("La longitud de onda no se encuentra dentro del espectro visible.")
elif 370 <= wavelenght < 449.9:
    color = "violeta"
elif 450 <= wavelenght < 494.9:
    color = "azul"
elif 495 <= wavelenght < 569.9:
    color = "verde"
elif 570 <= wavelenght < 589.9:
    color = "amarillo"
elif 590 <= wavelenght < 619.9:
    color = "naranja"
elif 620 <= wavelenght <= 750:
    color = "rojo"
else:
    print("La longitud de onda sobrepasa el espectro visible.")

print("El color asociado a su longitud de onda es", color)
