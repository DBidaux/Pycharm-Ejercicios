fcrear = open("pruebacreacion.txt", "w")
fcrear.write("Fichero creado desde cero\n")
fcrear.write("Keys Malaga\n")
fcrear.write("Fichero creado 8-2-4\n")
fcrear.close()

print("###Fichero creado###")

flectura = open("pruebacreacion.txt", "r")
texto = flectura.read()
flectura.close()
print(texto)
