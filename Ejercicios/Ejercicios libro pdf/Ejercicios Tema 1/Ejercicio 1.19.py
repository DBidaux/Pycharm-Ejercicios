from math import sqrt

altura_inicial = float(input("Indica la altura en metros desde la que se deja caer el objeto: "))
vel_inicial = 0
aceleracion = 9.8
velocidad_final = sqrt((vel_inicial ** 2) + 2 * aceleracion * altura_inicial)
print("La velocidad con la que el objeto golpea el suelo es de " + str(velocidad_final) + "m/s.")
