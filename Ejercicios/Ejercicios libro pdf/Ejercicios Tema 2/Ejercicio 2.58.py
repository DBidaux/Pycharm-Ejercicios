year = int(input("Introduzca un año: "))

if year % 400 == 0:
    bisiesto = True
elif year % 100 == 0:
    bisiesto = False
elif year % 4 == 0:
    bisiesto = True
else:
    bisiesto = False

mes = int(input("Introduzca un mes: "))

if mes in (1, 3, 5, 7, 8, 10, 12):
    diasmes = 31
elif mes == 2:
    if bisiesto:
        diasmes = 29
    else:
        diasmes = 28
else:
    diasmes = 30

dia = int(input("Introduzca un día: "))

if dia < diasmes:
    dia += 1
else:
    dia = 1
    if mes == 12:
        mes = 1
        year += 1

print("La fecha siguiente es " + str(year) + "-" + str(mes) + "-" + str(dia) + ".")
