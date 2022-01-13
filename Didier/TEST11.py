import sys

numero1 = input("Introduzca el primer número: ")
try:
    numero1 = int(numero1)
except:
    print("La conversión de este número no ha tenido éxito",
          file=sys.stderr)
    sys.exit()

try:
    numero2 = int(input("Introduzca el segundo número: "))
except ValueError as e:
    print("La conversión de este número no ha tenido éxito",
          file=sys.stderr)
    sys.exit()

if numero1 < numero2:
    print("El segundo número es mayor!")

elif numero1 > numero2:
    print("El primero numero es mayor!")

else:
    print("Son iguales!")
