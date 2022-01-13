distancia_en_pies = float(input("Introduzca la distancia en pies: "))
pulgada_por_pie = 12
pie_por_yarda = 3
pie_por_milla = 5280

print("La conversión de pies a pulgadas es: " + str(distancia_en_pies * pulgada_por_pie))
print("La conversión de pies a yardas es: " + str(distancia_en_pies / pie_por_yarda))
print("La conversión de pies a millas es: " + str(distancia_en_pies / pie_por_milla))
