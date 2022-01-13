edad = 27
trabajo = True
casado = False
ant_penales = False
if ant_penales != True:
    print("Tienes derecho a solicitar un préstamo")
else:
    print("No eres elegible a solicitar un préstamo")
print("----------")


print("Bienvenido a nuestro verificador de elegibilidad en línea!")
edad = int(input("Introduce tu edad:"))
carnet = input("Tienes carnet de conducir? [S/N]: ")
if carnet.lower() == "s":
    carnet = True
else:
    carnet = False
salario = int(input("Introduzca su salario mensual: "))
if edad <= 35:
    print("Edad correcta.")
    if carnet:
        print("Licencia válida.")
        if salario >= 3500:
            print("El salario está bien. Eres elegible.")
        else:
            print("Lo siento, estás por debajo de los requisitos mínimos.")
    else:
        print("Necesitas tener una licencia válida.")
else:
    print("Estás por encima del límite de edad máximo.")
print("----------")


print("Comprobador elegibilidad 101.")
nombre = input("Introduzca su nombre: ")
edad = int(input("Introduzca su edad: "))
salario = int(input("Introduzca su salario mensual: "))
salario_min = 5000
credito_ok = True
if salario >= salario_min or credito_ok:
    print(f"Es elegible para una hipoteca, {nombre} .")
else:
    print(f"{nombre}, no es elegible de momento")
print("----------")