cm_por_pulgada = 2.54
pulgada_por_pie = 12
pies = float(input("Introduce número de pies: "))
pulgada = float(input("Introduce numero de pulgadas: "))
cm = (pies * pulgada_por_pie + pulgada) + cm_por_pulgada
print("Su altura en cm es:", cm)
