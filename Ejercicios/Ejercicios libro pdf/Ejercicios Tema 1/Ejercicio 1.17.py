masa_agua = float(input("Introduzca la masa del agua en gramos: "))
incremento_temp = float(input("Introduzca el incremento de temperatura en grados Celcius: "))
calor_especifico = 4.186
q = masa_agua * calor_especifico * incremento_temp
J_por_kWh = 3600000
coste_energia = 0.089
coste_calentar = (q/J_por_kWh) * coste_energia
print("La cantidad de energia en julios es " + str(q) + " julios.")
print("El precio de calentar esa masa de agua es " + str(coste_calentar) + " céntimos.")