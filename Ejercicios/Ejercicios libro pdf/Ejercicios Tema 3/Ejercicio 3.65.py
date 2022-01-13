from math import sqrt

perimetro = 0
x_inicial = float(input("Introduce la parte x de la coordenada: "))
y_inicial = float(input("Introduce la parte y de la coordenada: "))

x_anterior = x_inicial
y_anterior = y_inicial

linea = input("Introduce la parte x de la coordenada (en blanco para salir): ")
while linea != "":
    x = float(linea)
    y = float(input("Introduce la parte y de la coordenada: "))
    dist = sqrt((x_anterior - x) ** 2 + (y_anterior - y) ** 2)
    perimetro = perimetro + dist
    x_anterior = x
    y_anterior = y
    linea = input("Introduce la parte x de la coordenada (en blanco para salir): ")

dist = sqrt((x_inicial - x) ** 2 + (y_inicial - y) ** 2)
perimetro = perimetro + dist
print("El perímetro del polígono es", perimetro)
