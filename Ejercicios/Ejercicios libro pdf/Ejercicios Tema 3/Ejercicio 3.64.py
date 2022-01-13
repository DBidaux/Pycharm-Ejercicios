pennies_per_nickel = 5
nickel = 0.5
total = 0
articulo = input("Introduzca el precio (en blanco para terminar): ")
while articulo != "":
    total = total + float(articulo)
    print(total)
    articulo = input("Introduzca el precio (en blanco para terminar): ")
print("El total a pagar con tarjeta es %.2f" % total)

redondeo = total * 100 % pennies_per_nickel
if redondeo < pennies_per_nickel / 2:
    efectivo = total - redondeo / 100
else:
    efectivo = total + nickel - redondeo / 100

print("El total a pagar en efectivo es %.2f" % efectivo)
