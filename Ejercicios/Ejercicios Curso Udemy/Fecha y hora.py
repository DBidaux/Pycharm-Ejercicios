#Fecha y hora

from datetime import datetime

fecha_y_hora = datetime.now()
print(fecha_y_hora)

ano = fecha_y_hora.year
mes = fecha_y_hora.month
dia = fecha_y_hora.day
hora = fecha_y_hora.hour
minuto = fecha_y_hora.minute
segundo = fecha_y_hora.second
print(ano, mes, dia, hora, minuto, segundo)
print("La hora es {}:{}:{}".format(hora, minuto, segundo))