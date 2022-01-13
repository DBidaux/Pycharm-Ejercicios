n_dias = int(input("Introduzca el número de días: "))
n_horas = int(input("Introduzca el número de horas: "))
n_minutos = int(input("Introduzca el número de minutos: "))
n_segundos = int(input("Introduzca el número de segundos: "))
seg_por_min = 60
seg_por_horas = seg_por_min * 60
seg_por_dias = seg_por_horas * 24
total_segundos = n_segundos + (n_minutos * seg_por_min) + (n_horas * seg_por_horas) + (n_dias * seg_por_dias)
print("El nº total de segundos del lapso de tiempo introducido es de " + str(total_segundos) + " segundos.")
