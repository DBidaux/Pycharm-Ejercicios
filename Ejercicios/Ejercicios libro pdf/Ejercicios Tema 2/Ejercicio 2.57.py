year = int(input("Introduzca un año para saber si es bisiesto o no: "))
cond_bisiesto_1 = year % 400
cond_no_bisiesto_1 = year % 100
cond_bisiesto_2 = year % 4

if cond_bisiesto_1:
    print("Es un año bisiesto")
elif cond_bisiesto_2:
    print("Es un año bisiesto")
elif cond_no_bisiesto_1:
    print("No es un año bisiesto")
else:
    print("No es un año bisiesto")

if year % 400 == 0:
    bisiesto = True
elif year % 100 == 0:
    bisiesto = False
elif year % 4 == 0:
    bisiesto = True
else:
    bisiesto = False

if bisiesto:
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")
