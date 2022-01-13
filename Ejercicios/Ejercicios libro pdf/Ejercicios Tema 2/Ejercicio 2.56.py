mensajestarifa = 50
minutostarifa = 50
preciotarifa = 15.00
precioinicial = 15.00
mensajeadd = 0.15
minutoadd = 0.25
tasa112 = 0.44
impuesto = 0.05

print("""--------------------------------------""")
mensajesusados = int(input("Introduzca los mensajes utilizados: "))
print("""--------------------------------------""")
if mensajesusados > mensajestarifa:
    mensajesextra = mensajesusados - mensajestarifa
    costemenextra = mensajesextra * mensajeadd
    preciotarifa += costemenextra

print("""--------------------------------------""")
minutosusados = float(input("Introduzca los minutos utilizados: "))
print("""--------------------------------------""")
if minutosusados > minutostarifa:
    minutosextra = minutosusados - minutostarifa
    costeminextra = minutosextra * minutoadd
    preciotarifa += costeminextra

total = preciotarifa + preciotarifa * 0.05

print("""--------------------------------------""")
print("Base imponible: $%.2f" % precioinicial)
try:
    print("Minutos adicionales: $%.2f" % costeminextra)
except NameError:
    pass

try:
    print("Mensajes adicionales: $%.2f" % costemenextra)
except NameError:
    pass

print("Tasa 112: $%.2f" % tasa112)
print("Impuestos: $%.2f" % impuesto)
print("Total: $%.2f" % preciotarifa)
print("""--------------------------------------""")