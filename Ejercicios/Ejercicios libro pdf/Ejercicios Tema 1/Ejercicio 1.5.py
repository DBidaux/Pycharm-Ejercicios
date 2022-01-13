envasep = 0.10
envaseg = 0.25

pequeno = int(input("¿Cuántas botellas de un litro o menos tienes?: "))
grande = int(input("¿Cuántas botellas de un litro o más tienes?: "))

devolucion = envasep * pequeno + envaseg * grande
print("Tu reembolso total será de €%.2f." % devolucion)
