explosion = 180
picapica = 130
cortacesped = 106
despertador = 70
habsil = 40
pisada = 10
sonido = int(input("Introduzca los decibelios: "))
if sonido < pisada:
    print("Su sonido es menor que una pisada.")
elif habsil < sonido < pisada:
    print("Su sonido se encuentra entre una pisada y una habitación en silencio.")
elif habsil < sonido < despertador:
    print("Su sonido se encuentra entre una habitación en silencio y un despertador.")
elif despertador < sonido < cortacesped:
    print("Su sonido se encuentra entre un despertador y un cortacésped.")
elif cortacesped < sonido < picapica:
    print("Su sonido se encuentra entre un cortacésped y un martillo neumático.")
else:
    print("Su sonido es superior a una explosión.")
