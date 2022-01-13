# Season from month and day
mes = input("Introduzca el nombre del mes: ")
dia = int(input("Introduzca el número del día: "))

if mes == "Enero" or mes == "Febrero":
    estacion = "Invierno"
elif mes == "Marzo":
    if dia < 20:
        estacion = "Invierno"
    else:
        estacion = "Primavera"

elif mes == "Abril" or mes == "Mayo":
    estacion = "Primavera"
elif mes == "Junio":
    if dia < 21:
        estacion = "Primavera"
    else:
        estacion = "Verano"

elif mes == "Julio" or mes == "Agosto":
    estacion = "Verano"
elif mes == "Septiembre":
    if dia < 22:
        estacion = "Verano"
    else:
        estacion = "Otoño"

elif mes == "Octubre" or mes == "Noviembre":
    estacion = "Otoño"
elif mes == "Diciembre":
    if dia < 21:
        estacion = "Otoño"
    else:
        estacion = "Invierno"

print("El " + str(dia), "de " + mes + " es " + str(estacion))
