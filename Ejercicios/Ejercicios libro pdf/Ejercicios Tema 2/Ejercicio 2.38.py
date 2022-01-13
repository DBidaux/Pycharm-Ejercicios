mes = input("Introduce el nombre de un mes: ")
if mes == "Enero" or mes == "Marzo" or mes == "Mayo" or mes == "Julio" or mes == "Agosto" or mes == "Octubre" or mes == "Diciembre":
    print("Este mes tiene 31 días.")
elif mes == "Abril" or mes == "Junio" or mes == "Septiembre" or mes == "Noviembre":
    print("Este mes tiene 30 días.")
elif mes == "Febrero":
    print("Tiene 28 o 29 días, dependiendo si el año es bisiesto o no.")
