Washington = 1
Jefferson = 2
Lincoln = 5
Hamilton = 10
Jackson = 20
Grant = 50
Franklin = 100

billete = int(input("Introduzca el valor del billete: "))

if billete == 1:
    print("La persona que aparece en el billete es Washington.")
elif billete == 2:
    print("La persona que aparece en el billete es Jefferson.")
elif billete == 5:
    print("La persona que aparece en el billete es Lincoln.")
elif billete == 10:
    print("La persona que aparece en el billete es Hamilton.")
elif billete == 20:
    print("La persona que aparece en el billete es Jackson.")
elif billete == 50:
    print("La persona que aparece en el billete es Grant.")
elif billete == 100:
    print("La persona que aparece en el billete es Franklin.")
else:
    print("No hay moneda en curso de ese valor.")
