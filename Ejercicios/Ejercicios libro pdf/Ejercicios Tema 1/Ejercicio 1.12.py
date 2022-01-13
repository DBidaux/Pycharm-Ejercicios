from math import acos, sin, cos, radians

lat1 = radians(float(input("Introduce la latitud en grados º del primer punto: ")))
lon1 = radians(float(input("Introduce la longitud en grados º del primer punto: ")))
lat2 = radians(float(input("Introduce la latitud en grados º del segundo punto: ")))
lon2 = radians(float(input("Introduce la longitud en grados º del segundo punto: ")))

Distancia = 6371.01 * acos(sin(lat1) * sin(lat2) + cos(lon1) * cos(lon2) * cos(lon1 - lon2))
print("La distancia en kilómetros es %.2f km." % Distancia)
