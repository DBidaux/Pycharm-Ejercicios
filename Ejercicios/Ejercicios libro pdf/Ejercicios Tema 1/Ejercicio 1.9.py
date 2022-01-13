saldo_cuenta = float(input("Introduzca el total del saldo de la cuenta: "))
interes = 0.04
tiempo = round(float(input("Introduzca el número de años: ")))
saldo_final = round(saldo_cuenta * (1 + interes) ** tiempo)
ingreso = float(input("Introduzca la cantidad de dinero que ingresará anualmente: "))
ingreso_cuenta = saldo_final + (ingreso*tiempo)
print("El saldo final de la cuenta de ahorro tras " + str(tiempo) + " años " + "es de: " + str(ingreso_cuenta) + "€.")
