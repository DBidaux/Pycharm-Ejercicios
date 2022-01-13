peso = float(input("Introduzca su peso en kg: "))
altura = float(input("Introduzca su altura en metros: "))

imc = (peso / (altura * altura))

print("Su IMC es de: " + str(imc))
