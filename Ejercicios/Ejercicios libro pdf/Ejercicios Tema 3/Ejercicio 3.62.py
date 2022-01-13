porcentaje = 0.6
precio_ori = [4.95, 9.95, 14.95, 19.95, 24.95, ]
print(precio_ori)
print("El porcentaje de descuento es " + str(porcentaje))

for precio in precio_ori:
    precio_final = porcentaje * precio
    print("Precio final: %.2f" % precio_final)
