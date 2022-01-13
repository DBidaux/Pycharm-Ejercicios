# Birth to astrological sign
mes = input("Introduzca el nombre del mes: ")
dia = int(input("Introduzca el número del día: "))

if mes == "Diciembre":
    signo = "Sagitario" if (dia < 22) else "Capricornio"
elif mes == "Enero":
    signo = "Capricornio" if (dia < 20) else "Acuario"
elif mes == "Febrero":
    signo = "Acuario" if (dia < 19) else "Piscis"
elif mes == "Marzo":
    signo = "Piscis" if (dia < 21) else "Aries"
elif mes == "Abril":
    signo = "Aries" if (dia < 20) else "Tauro"
elif mes == "Mayo":
    signo = "Tauro" if (dia < 21) else "Géminis"
elif mes == "Junio":
    signo = "Géminis" if (dia < 21) else "Cáncer"
elif mes == "Julio":
    signo = "Cáncer" if (dia < 23) else "Leo"
elif mes == "Agosto":
    signo = "Leo" if (dia < 23) else "Virgo"
elif mes == "Septiembre":
    signo = "Virgo" if (dia < 23) else "Libra"
elif mes == "Octubre":
    signo = "Libra" if (dia < 23) else "Escorpio"
else:
    signo = "Escorpio" if (dia < 22) else "Sagitario"

print("Tu horóscopo según tu fecha de nacimiento es:", signo)
