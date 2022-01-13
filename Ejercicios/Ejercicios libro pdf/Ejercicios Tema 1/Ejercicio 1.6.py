precio_plato = float(input("Introduzca el precio del ticket en €: "))
iva = precio_plato * 0.21
propina = precio_plato * 0.18
total = precio_plato + iva + propina

print("El IVA del ticket es de %.2f." % iva)
print("La propina del ticket es de €%.2f." % propina)
print("El total del ticket es de €%.2f." % total)
