segundos_dia = 86400
segundos_hora = 3600
segundos_minuto = 60

segundos = int(input("Introduzca el número de segundos: "))

dias = segundos / segundos_dia
segundos = segundos % segundos_dia

horas = segundos / segundos_hora
segundos = segundos % segundos_hora

minutos = segundos / segundos_minuto
segundos = segundos % segundos_minuto

print("El esquivalente en DD:HH:MM:SS es " + " %d:%02d:%02d:%02d" % (dias, horas, minutos, segundos))

# El formato de %02d especifica a Python como debe formatear el numero entero
# usando dos dígitos añadiendo un 0 delante si es necesario.
