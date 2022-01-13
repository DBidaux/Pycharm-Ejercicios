# Módulo datetime: fechas
# datetime.now: fecha y hora actual.
# date.today: día actual.
# date: crea objeto fecha, introduciéndole año, mes y día.
# datetime: crea objeto tipo datetime, introduciendo año, mes, dia, hora, minuto, segundo, y microseg.

import datetime
print("----------Ejercicio 1:----------")
print("Ahora mismo es: ", datetime.datetime.now())
print("Hoy es: ", datetime.datetime.today())
fecha = datetime.date(2021, 5, 20)
print(fecha)
fechahora = datetime.datetime(2021, 5, 20, 19, 10, 000, 0000)
print(fechahora)

print("----------Ejercicio 2:----------")
fecha = datetime.datetime(2016, 2, 21, 14, 00, 00, 000)
print(fecha)
print("Año: ", fecha.year)
print("Mes: ", fecha.month)
print("Día: ", fecha.day)
print("Hora: ", fecha.hour)
print("Minutos: ", fecha.minute)
print("Segundos: ", fecha.second)
print("Microsegundos: ", fecha.microsecond)

print("----------Ejercicio 3:----------")
fin = datetime.datetime.now()
inicio = datetime.datetime(2016, 2, 21, 14, 00, 00, 000)
print("Resta de fechas: ")
print("1.- ", fin)
print("2.- ", inicio)
resultado = fin - inicio
print("Resultado: ", resultado)