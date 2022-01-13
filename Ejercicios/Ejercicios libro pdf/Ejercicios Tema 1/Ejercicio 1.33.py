n_barras_viejas = int(input("¿Cuántas barras de ayer lleva el cliente?: "))
n_barras_hoy = int(input("¿Cuántas barras de hoy lleva el cliente?: "))
precio_barra_dia = 3.49
precio_barra_ayer = precio_barra_dia * 0.6
total = (n_barras_viejas * precio_barra_ayer) + precio_barra_dia
print("El precio de la barra es 3.49€, al ser de ayer, tiene descuento. Tu total es de: %.2f€." % total)
