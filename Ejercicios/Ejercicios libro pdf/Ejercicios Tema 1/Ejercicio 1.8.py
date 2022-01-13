widgets = 75
gizmos = 112

n_widgets = int(input("Introduzca el número de wigdets: "))
n_gizmos = int(input("Introduzca el número de gizmos: "))
peso_widgets = n_widgets * widgets
peso_gizmos = n_gizmos * gizmos
peso_total_gramos = int(peso_gizmos + peso_widgets)
peso_total_kilos = float(peso_total_gramos / 100)
print("El peso total del pedido en gramos es %.2f gr." % peso_total_gramos)
print("El peso total del pedido en kilos es %.2f kg." % peso_total_kilos)
