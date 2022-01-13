euro = 100
cinq = 50
veint = 20
diez = 10
cinc = 5
dos = 2
uno = 1

centimos = int(input("Introduzca el número de céntimos: "))
print(" ", centimos // euro)
centimos = centimos % euro

print(" ", centimos // cinq)
centimos = cinq % euro

print(" ", centimos // veint)
centimos = centimos % veint

print(" ", centimos // diez)
centimos = centimos % diez

print(" ", centimos // cinc)
centimos = centimos % cinc

print(" ", centimos // dos)
centimos = centimos % dos

print(" ", centimos // uno)
centimos = centimos % uno