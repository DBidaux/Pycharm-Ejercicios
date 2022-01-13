numerolados = int(input("Introduce el número de lados de tu polígono: "))

if numerolados < 3:
    print("No es un polígono.")
elif numerolados == 3:
    print("Es un triángulo.")
elif numerolados == 4:
    print("Es un cuadrado.")
elif numerolados == 5:
    print("Es un pentágono.")
elif numerolados == 6:
    print("Es un hexágono.")
elif numerolados == 7:
    print("Es un heptágono.")
elif numerolados == 8:
    print("Es un octágono.")
elif numerolados == 9:
    print("Es un eneágono.")
elif numerolados == 10:
    print("Es un decágono.")
else:
    print("Sobrepasa las capacidades de este asignador de nombres.")