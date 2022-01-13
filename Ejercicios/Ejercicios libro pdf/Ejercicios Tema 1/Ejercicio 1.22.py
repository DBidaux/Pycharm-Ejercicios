from math import sqrt

lado1 = float(input("Introduce la altura en cm del primer lado: "))
lado2 = float(input("Introduce la altura en cm del segundo lado: "))
lado3 = float(input("Introduce la altura en cm del tercer lado: "))
total_lados = (lado1 + lado2 + lado3) / 2
area_tr_lados = sqrt(total_lados * (total_lados - lado1) * (total_lados - lado2) * (total_lados - lado3))
print("El área del triángulo es de " + str(area_tr_lados) + " cm2.")
